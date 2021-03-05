#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re, sys, traceback
from datetime import datetime
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches
#import pprint


class DefaultConfig:
    # color: 'k', 'grey', 'brown', 'darkred', 'r', 'orange', 'gold', 'y', 'yellowgreen', 'g', 'lime', springgreen', 'c', 'darkcyan',
    #       'skyblue', 'steelblue', 'navy', 'b', 'violet', 'purple', 'm', 'pink', 'deeppink'
    # component: [(priority, [(id, color, {'same_core': False, 'show': False, 'xtick': True}), ...]), ...]
    TRACES_CONFIG = {
        'RADIO PROC': [(1, 'Offloading', [(('NR_L0_RADIO_PROC_OFFLOADING_START', 'NR_L0_RADIO_PROC_OFFLOADING_END'), 'b', {'show': False})]),
                       (2, 'RadioProc', [(('NR_L0_RADIO_PROC_START', 'NR_L0_RADIO_PROC_END'), 'g', {})]),
                      ],
        'DL SRP': [(10, 'DlSrp FFT', [(('NR_L0_DLSRP_DL_FFT_DATA_START', 'NR_L0_DLSRP_DL_FFT_DATA_END'), 'r', {})]),
                   (11, 'DlSrp Pdcch', [(('NR_L0_DLSRP_PDCCH_START', 'NR_L0_DLSRP_PDCCH_END'), 'm', {'xtick': True})]),
                  ],
        'PDCCH': [(20, 'Pdcch Brp', [(('NR_L0_DLC_PDCCH_BRP_START', 'NR_L0_DLC_PDCCH_BRP_SD_END'), 'k', {})]),
                  (21, 'Pdcch Copro', [(('NR_L0_DLC_COPRO_DECODE_START', 'NR_L0_DLC_COPRO_DECODE_END'), 'c', {'same_core': False})]),
                  (22, 'Pdcch Copro Cnf', [(('NR_L0_DLC_COPRO_CNF_TASK_START', 'NR_L0_DLC_COPRO_CNF_TASK_END'), 'y', {})]),
                  (23, 'Pdcch Sd Result', [(('NR_L0_DLC_SD_TASK_RSLT_START', 'NR_L0_DLC_SD_TASK_RSLT_END'), 'b', {}),
                                           ('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0L1_PHY_DLC_UL_SCH_DATA_READY_IND'})]),
                 ],
        'PDSCH BRP': [(30, 'Pdsch Copro', [(('NR_L0_PDSCHBRP_COPRO_START', 'NR_L0_PDSCHBRP_COPRO_END'), 'b', {'show': False})]),
                      (31, 'Pdsch Copro Req', [(('NR_L0_PDSCHBRP_COPRO_REQ_START', 'NR_L0_PDSCHBRP_COPRO_REQ_END'), 'g', {})]),
                      (32, 'Pdsch Copro Cnf', [(('NR_L0_PDSCHBRP_COPRO_CNF_START', 'NR_L0_PDSCHBRP_COPRO_CNF_END'), 'r', {'show': False})]),
                      (33, 'Pdsch Post', [(('NR_L0_PDSCHBRP_POST_PROCESS_START', 'NR_L0_PDSCHBRP_POST_PROCESS_END'), 'm', {}),
                                          ('NR_L0_PDSCHBRP_PHY_IND', 'r', {})]),
                      (34, 'Pdsch Msg', [('NR_L0_PDSCHBRP_PHY_IND_CRC_RESULTS', 'k', {'show': False})]),
                      (35, 'HARQ Msg', [('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0_ULC_DLC_SEND_HARQ_IND'})]),
                     ],
        'UL CTRL': [(40, 'UlCtrl Tti', [(('NR_L0_ULC_SCHEDULE_TTI_START', 'NR_L0_ULC_SCHEDULE_TTI_END'), 'c', {})]),
                   ],
        'UL BRP':  [(50, 'UCP Msg', [('NR_L0_ULBRP_UCP_REQ_MSG_SENT', 'm', {}),
                                     ('NR_L0_ULBRP_UCP_HARQ_REQ_MSG_SENT', 'y', {}),
                                     ('NR_L0_ULBRP_UCP_CSI_REQ_MSG_SENT', 'b', {})]),
                    (51, 'PUCCH Data', [('NR_L0_ULBRP_SEND_MAP_PUCCH_DATA_MSG', 'r', {})]),
                   ],
        'UL SRP': [(60, 'UlSrp Mapping', [(('NR_L0_ULSRP_PUSCH_MAPPING_START', 'NR_L0_ULSRP_PUSCH_MAPPING_END'), 'c', {}),
                                          (('NR_L0_ULSRP_PUCCH_MAPPING_START', 'NR_L0_ULSRP_PUCCH_MAPPING_END'), 'r', {}),
                                          (('NR_L0_ULSRP_SRS_MAPPING_START', 'NR_L0_ULSRP_SRS_MAPPING_END'), 'g', {})]),
                   (61, 'UlSrp Tick', [(('NR_L0_ULSRP_TICK_HANDLING_START', 'NR_L0_ULSRP_TICK_HANDLING_END'), 'k', {}),
                                       ('NR_L0_ULSRP_TIMING_SLOT', 'r', {})]),
                  ],
                  }

    TRACES_FORMAT = {
        'NR_L0_RADIO_PROC_OFFLOADING_START': (['RadioStreamIdx', 'Lst'], ['ant', 'start_lst']),
        'NR_L0_RADIO_PROC_OFFLOADING_END': (['BClk'], ['bclk']),
        'NR_L0_RADIO_PROC_START': (['RadioStreamIdx', 'Lst'], ['ant', 'start_lst']),
        'NR_L0_RADIO_PROC_END': (['RadioStreamIdx', 'Lst'], ['ant', 'end_lst']),
        'NR_L0_DLSRP_DL_FFT_DATA_START': (['Hwi', 'RadioStreamIdx', 'Lst'], ['hwi', 'ant', 'start_lst']),
        'NR_L0_DLSRP_DL_FFT_DATA_END': (['Hwi', 'RadioStreamIdx', 'Lst'], ['hwi', 'ant', 'start_lst']),
        'NR_L0_DLSRP_PDCCH_START': (['Sfn', 'Subframe', 'Slot', 'Symbol', 'Hwi', 'TaskIndex'], ['sfn', 'subframe', 'slot', 'symbol', 'hwi', 'task_index']),
        'NR_L0_DLSRP_PDCCH_END': (['Sfn', 'Subframe', 'Slot', 'Symbol', 'Hwi', 'TaskIndex'], ['sfn', 'subframe', 'slot', 'symbol', 'hwi', 'task_index']),
        'NR_L0_DLC_PDCCH_BRP_START': (['Sfn', 'SubframeNum', 'SlotNum'], ['sfn', 'subframe', 'slot']),
        'NR_L0_DLC_PDCCH_BRP_SD_END': (['Sfn', 'SubframeNum', 'SlotNum'], ['sfn', 'subframe', 'slot']),
        'NR_L0_DLC_COPRO_DECODE_START': (['SubframeNum', 'SlotNum'], ['subframe', 'slot']),
        'NR_L0_DLC_COPRO_DECODE_END': (['SubframeNum', 'SlotNum'], ['subframe', 'slot']),
        'NR_L0_DLC_COPRO_CNF_TASK_START': (['SubframeNum', 'SlotNum'], ['subframe', 'slot']),
        #'NR_L0_DLC_COPRO_CNF_TASK_END': ([], []),
        'NR_L0_DLC_SD_TASK_RSLT_START': (['Sfn', 'SubframeNum', 'SlotNum', 'TaskId'], ['sfn', 'subframe', 'slot', 'task_index']),
        'NR_L0_DLC_SD_TASK_RSLT_END': (['Sfn', 'SubframeNum', 'SlotNum', 'TaskId'], ['sfn', 'subframe', 'slot', 'task_index']),
        'NR_L0_PDSCHBRP_COPRO_START': (['SubframeNum', 'CbIndex'], ['subframe', 'cb_index']),
        'NR_L0_PDSCHBRP_COPRO_END': (['SubframeNum', 'CbIndex'], ['subframe', 'cb_index']),
        'NR_L0_PDSCHBRP_COPRO_REQ_START': (['Subframe', 'Slot', 'CbIndex'], ['subframe', 'slot', 'cb_index']),
        'NR_L0_PDSCHBRP_COPRO_REQ_END': (['CbIndex'], ['cb_index']),
        'NR_L0_PDSCHBRP_COPRO_CNF_START': (['Subframe', 'Slot', 'CbIndex'], ['subframe', 'slot', 'cb_index']),
        'NR_L0_PDSCHBRP_COPRO_CNF_END': (['CbIndex'], ['cb_index']),
        'NR_L0_PDSCHBRP_POST_PROCESS_START': (['Subframe', 'Slot', 'CwIndex', 'CbIndex'], ['subframe', 'slot', 'cw_index', 'cb_index']),
        'NR_L0_PDSCHBRP_POST_PROCESS_END': (['CwIdx', 'CbIdx'], ['cw_index', 'cb_index']),
        'NR_L0_ULC_SCHEDULE_TTI_START': (['Sfn', 'Subframe', 'Slot'], ['sfn', 'subframe', 'slot']),
        'NR_L0_ULC_SCHEDULE_TTI_END': (['Sfn', 'Subframe', 'Slot'], ['sfn', 'subframe', 'slot']),
        'NR_L0_ULSRP_PUSCH_MAPPING_START': (['Sfn', 'Subframe', 'Slot', 'Symbol'], ['sfn', 'subframe', 'slot', 'symbol']),
        'NR_L0_ULSRP_PUSCH_MAPPING_END': (['Sfn', 'Subframe', 'Slot', 'Symbol'], ['sfn', 'subframe', 'slot', 'symbol']),
        'NR_L0_ULSRP_PUCCH_MAPPING_START': (['Sfn', 'Subframe', 'Slot'], ['sfn', 'subframe', 'slot']),
        'NR_L0_ULSRP_PUCCH_MAPPING_END': (['Sfn', 'Subframe', 'Slot'], ['sfn', 'subframe', 'slot']),
        'NR_L0_ULSRP_SRS_MAPPING_START': (['Sfn', 'Subframe', 'Slot', 'Symbol'], ['sfn', 'subframe', 'slot', 'symbol']),
        'NR_L0_ULSRP_SRS_MAPPING_END': (['Sfn', 'Subframe', 'Slot', 'Symbol'], ['sfn', 'subframe', 'slot', 'symbol']),
        'NR_L0_ULSRP_TICK_HANDLING_START': (['UlStream', 'RpuIndex', 'Hwi', 'Instance'], ['stream', 'rpu_index', 'hwi', 'instance']),
        'NR_L0_ULSRP_TICK_HANDLING_END': (['UlStream', 'RpuIndex', 'Hwi', 'Instance'], ['stream', 'rpu_index', 'hwi', 'instance']),
        }

class EventsConfig:
    def __init__(self, config = None):
        if config is None: config = DefaultConfig
        self.traces_config = config.TRACES_CONFIG if hasattr(config, 'TRACES_CONFIG') else DefaultConfig.TRACES_CONFIG
        self.traces_format = config.TRACES_FORMAT if hasattr(config, 'TRACES_FORMAT') else DefaultConfig.TRACES_FORMAT
        self.init_events_config()

    @staticmethod
    def get_rand_color(except_color = []):
        color_list = ['r', 'g', 'b', 'c', 'y', 'm', 'brown', 'purple', 'navy', 'darkcyan', 'gold', 'orange', 'lime', 'springgreen',
           'skyblue', 'yellowgreen', 'steelblue', 'violet', 'pink', 'deeppink', 'k', 'grey']
        for color in color_list:
            if not color in except_color:
                break
        return color

    def get_option(self, option):
        def _set_default_option(item, value):
            if not item in option: option[item] = value
        _set_default_option('same_core', True)
        _set_default_option('show', True)
        _set_default_option('xtick', False)
        _set_default_option('combine_core', False)
        _set_default_option('rand_core_color', False)
        _set_default_option('filter', '')
        return option

    def init_events_config(self):
        self.init_traces_format()
        self.events_config = {}
        self.trace_id_with_filters = {}
        for component, events in self.traces_config.items():
            for priority, event_name, traces in events:
                event_config = EventConfig(component, priority, event_name, self)
                for trace_id, color, option in traces:
                    option = self.get_option(option)
                    if not option['show']: continue
                    if option['filter']:
                        unique_trace_id = '%s__%s' % (trace_id, option['filter'])   # change trace_id to make it unique if filter exists
                        if trace_id in self.trace_id_with_filters:
                            self.trace_id_with_filters[trace_id].append(unique_trace_id)
                        else:
                            self.trace_id_with_filters[trace_id] = [unique_trace_id]
                        trace_id = unique_trace_id
                    event_config.set_trace(trace_id, color, option)
                    trace_id_list = list(trace_id) if isinstance(trace_id, tuple) else [trace_id]
                    for id in trace_id_list:
                        self.events_config[id] = event_config
        #pprint.pprint(self.events_config)

    def init_traces_format(self):
        self.traces_re_pattern = {}
        for key, (raw_items, to_items) in self.traces_format.items():
            self.traces_re_pattern[key] = ''
            for item in raw_items:
                self.traces_re_pattern[key] += '%s:\s*([-\d]+).*' % item
            #pprint.pprint(key + self.traces_re_pattern[key])
        self.traces_re = {}
        for key, pattern in self.traces_re_pattern.items():
            self.traces_re[key] = re.compile(pattern)

    def get_event_config(self, trace_id):
        return self.events_config[trace_id] if trace_id in self.events_config else None

    def get_unique_trace_id(self, trace_id, params_text):
        if trace_id in self.events_config:
            return trace_id
        if params_text and trace_id in self.trace_id_with_filters:
            for unique_trace_id in self.trace_id_with_filters[trace_id]:
                filter = self.events_config[unique_trace_id].traces[unique_trace_id].filter
                r = re.search(filter, params_text)
                if r: return unique_trace_id
        return None

    def get_trace_params(self, trace_id, params_text):
        params = {}
        event_config = self.events_config[trace_id]
        if trace_id in event_config.traces_re_pattern:
            r = self.traces_re[trace_id].search(params_text)
            assert r, '[%s] cannot find pattern "%s" in "%s"' % (trace_id, event_config.traces_re_pattern[trace_id], params_text)
            for i in range(len(r.groups())):
                params[event_config.traces_format[trace_id][1][i]] = r.group(i+1)
        return params

class TraceConfig:
    def __init__(self, id, color, option, type):
        self.id = id
        self.color = color
        self.type = type
        self.same_core = option['same_core']
        self.show = option['show']
        self.combine_core = option['combine_core']
        self.rand_core_color = option['rand_core_color']
        self.filter = option['filter']
        self.xtick = False if self.type == 'end' else option['xtick']   # do not use end trace to tick

class EventConfig:
    def __init__(self, component, priority, name, events_config):
        self.component = component
        self.priority = priority
        self.name = name
        self._events_config = events_config
        self.traces_id = []
        self.traces = {}
        self.traces_re_pattern = {}
        self.traces_format = {}

    def _set_trace(self, trace_id, color, option, type = 'info'):
        self.traces[trace_id] = TraceConfig(trace_id, color, option, type)
        self.traces_id.append(trace_id)
        if trace_id in self._events_config.traces_format:
            self.traces_re_pattern[trace_id] = self._events_config.traces_re_pattern[trace_id]
            self.traces_format[trace_id] = self._events_config.traces_format[trace_id]

    def set_trace(self, trace_id, color, option):
        self.option = option
        if isinstance(trace_id, tuple):
            start_trace_id, end_trace_id = trace_id
            self._set_trace(start_trace_id, color, option, 'start')
            self._set_trace(end_trace_id, color, option, 'end')
        else:
            self._set_trace(trace_id, color, option)

    def has_start_trace(self):
        return not self.get_start_trace_id() is None

    def get_start_trace_id(self):
        for trace_id, trace_config in self.traces.items():
            if trace_config.type == 'start':
                return trace_id
        return None

    def get_end_trace_id(self):
        for trace_id, trace_config in self.traces.items():
            if trace_config.type == 'end':
                return trace_id
        return None

    def __str__(self):
        s = '[%s] Priority %d\n' % (self.component, self.priority)
        for trace_config in self.traces:
            s += '%s, type: %d, color: %s, same_core: %s, show: %s, xtick: %s, filter: %s\n' \
                % (trace_config.id, trace_config.type, trace_config.color, trace_config.same_core, trace_config.show, trace_config.xtick, trace_config.filter)
        return s

class Trace:
    def __init__(self, time, hwi, server, core, id, params_text, raw_text):
        self.time = time
        self.hwi = hwi
        self.server = server
        self.core = core
        self.id = id
        self.params_text = params_text
        self.raw_text = raw_text
        self.params = g_events_config.get_trace_params(id, params_text)
        self.event_config = g_events_config.get_event_config(id)
        self.trace_config = self.event_config.traces[id]
        self.type = self.trace_config.type
        if self.type == 'info':
            self.time_range = (time, time + 2)
        else:
            self.time_range = (time, time)  # 'start' or 'end'

    @staticmethod
    def is_valid_id(id, params_text = ''):
        return g_events_config.get_unique_trace_id(id, params_text)

    def is_the_same_event(self, trace):
        same_core = self.trace_config.same_core
        same_event = (trace.hwi == self.hwi and trace.server == self.server and (trace.core == self.core or not same_core) and trace.id in self.event_config.traces_id)
        if same_event:
            for item, value in trace.params.items():
                if item in self.params and self.params[item] != value:
                    print('Trace Id "%s" params not match! item "%s", "%s" - "%s".' % (trace.id, item, trace.params[item], self.params[item]))
                    return False
        return same_event

    def __str__(self):
        #s = '[%s] HLC %d.%d, %.2fus: %s%s\n' % (self.event_config.component, self.server, self.core, self.time, self.id, self.params_text)
        return '%s\n' % self.raw_text

class Event:
    def __init__(self, trace, rand_color_dict = {}):
        if trace.type == 'start':
            self.start_trace = trace
            self.info_traces = []
            self.finish_flag = False
        else:
            self.info_traces = [trace]
            self.finish_flag = True
        self.time_range = trace.time_range
        self.server = trace.server
        self.core = trace.core
        self.event_config = trace.event_config
        self.show = trace.trace_config.show
        self.xticks = [trace.time] if trace.trace_config.xtick else []
        self.event_time_text = None
        self.retain_event_time_text = False
        self.set_rand_color(rand_color_dict, trace.trace_config.color)

    def set_rand_color(self, rand_color_dict, trace_color):
        if self.event_config.option['rand_core_color']:
            if not self.event_config.priority in rand_color_dict:
                rand_color_dict[self.event_config.priority] = {}
            key = (self.server, self.core)
            if key in rand_color_dict[self.event_config.priority]:
                self.color = rand_color_dict[self.event_config.priority][key]
            elif not rand_color_dict[self.event_config.priority]:
                rand_color_dict[self.event_config.priority][key] = trace_color
                self.color = trace_color
            else:
                color = EventsConfig.get_rand_color(rand_color_dict[self.event_config.priority].values())
                rand_color_dict[self.event_config.priority][key] = color
                self.color = color

    def try_add_trace(self, trace):
        if self.finish_flag: return False
        if trace.time > self.start_trace.time and self.start_trace.is_the_same_event(trace):
            if trace.type == 'end':
                self.end_trace = trace
                self.finish_flag = True
            else:
                self.info_traces.append(trace)
            self.time_range = (min(self.time_range[0], trace.time_range[0]), max(self.time_range[1], trace.time_range[1]))
            self.show = self.show or trace.trace_config.show
            if trace.trace_config.xtick: self.xticks.append(trace.time)
            return True
        return False

    def shrink(self, text):
        MIN_DOTS_NUM = 10
        def _shrink_dots(s): return s.group(0)[0] + '.' * (len(s.group(1)) + MIN_DOTS_NUM - num_min_dots)
        dots_list = re.findall('\w(\.{3,100})\s', text)
        num_min_dots = min(map(len, dots_list))
        if 3 <= num_min_dots <= 100:
            text = re.sub('\w(\.{3,100})\s', _shrink_dots, text)
        return text

    def __str__(self):
        s = ''
        if hasattr(self, 'start_trace'): s += str(self.start_trace)
        for trace in self.info_traces:
            s += str(trace)
        if hasattr(self, 'end_trace'): s += str(self.end_trace)
        s = self.shrink(s)
        return s

    def set_line_index(self, line_index, total_lines):
        self.line_index = line_index
        self.total_lines = total_lines
        if hasattr(self, 'start_trace'):
            self.rect_region = (self.time_range[0], self.time_range[1], self.total_lines - self.line_index - 1, self.total_lines - self.line_index)
        else:
            trace = self.info_traces[0]
            self.rect_region = (trace.time_range[0], trace.time_range[1], self.total_lines - self.line_index - 1, self.total_lines - self.line_index)

    def draw(self, pic):
        self.pic = pic
        if hasattr(self, 'start_trace'):
            rect_region = (self.time_range[0], self.time_range[1], self.total_lines - self.line_index - 1, self.total_lines - self.line_index)
            color = self.color if hasattr(self, 'color') else self.start_trace.trace_config.color
            pic.draw_rect(rect_region, color)
        for trace in self.info_traces:
            rect_region = (trace.time_range[0], trace.time_range[1], self.total_lines - self.line_index - 1, self.total_lines - self.line_index)
            #color = self.color if hasattr(self, 'color') else trace.trace_config.color
            color = trace.trace_config.color
            pic.draw_rect(rect_region, color)

    def is_in_rect_region(self, x, y):
        return self.rect_region[0] <= x <= self.rect_region[1] and self.rect_region[2] <= y <= self.rect_region[3]

    def on_focus(self):
        self.pic.event_text.set_text(str(self))
        if not self.event_time_text:
            self.event_time_text = self.pic.ax.text(self.rect_region[0], self.rect_region[3] + 0.3, '%.1fus' % (self.rect_region[1] - self.rect_region[0]), fontsize = 11, color = 'b')
            self.pic.flush()

    def out_focus(self):
        if self.event_time_text and not self.retain_event_time_text:
            self.event_time_text.remove()
            self.event_time_text = None
            self.pic.flush()

    def on_dblclick(self):
        if self.event_time_text:
            self.retain_event_time_text = not self.retain_event_time_text
            color = 'r' if self.retain_event_time_text else 'b'
            self.event_time_text.set_color(color)
            self.pic.flush()

class Events:
    def __init__(self):
        self.current_event = None
        self.rand_color_dict = {}
        self.reset()

    def reset(self):
        self.event_list_pending_index = []  # optimize the time consuming
        self.event_list = []

    def add_trace(self, trace):
        if trace.type == 'start' or not trace.event_config.has_start_trace():
            event = Event(trace, self.rand_color_dict)
            if not event.finish_flag: self.event_list_pending_index.append(len(self.event_list))
            self.event_list.append(event)
            return True
        else:
            for index in self.event_list_pending_index:
                event = self.event_list[index]
                if event.try_add_trace(trace):
                    if event.finish_flag: self.event_list_pending_index.remove(index)
                    return True
            if trace.type == 'end':
                print('Warning: Trace Id cannot be added! %s.' % trace.raw_text)
                return False
            event = Event(trace, self.rand_color_dict)
            if not event.finish_flag: self.event_list_pending_index.append(len(self.event_list))
            self.event_list.append(event)
            return True

    def statistics(self):
        self.time_range = None
        self.draw_event_list = []
        self.group = {} # key is (priority, server, core), each group occupies one line
        for event in self.event_list:
            if not event.finish_flag or not event.show: continue  # do not draw event not finished
            self.time_range = event.time_range if self.time_range is None else (min(self.time_range[0], event.time_range[0]), max(self.time_range[1], event.time_range[1]))
            #print(event)
            if event.event_config.option['combine_core']:
                key = (event.event_config.priority, event.server, '*')
            else:
                key = (event.event_config.priority, event.server, event.core)
            if key in self.group:
                self.group[key].append(event)
            else:
                self.group[key] = [event]
            self.draw_event_list.append(event)
        #pprint.pprint(self.group)
        sorted_keys = sorted(self.group.keys())
        self.yticks_label = []
        self.xticks = []
        self.xticks_server = None
        # we only enable xticks from one server
        self.total_lines = len(self.group)
        for line_index, key in enumerate(sorted_keys):  # key is (priority, server, core)
            for event in self.group[key]:
                event.set_line_index(line_index, self.total_lines)
                if event.xticks:
                    if not self.xticks_server:
                        self.xticks_server = event.server
                        self.xticks += event.xticks
                    elif self.xticks_server == event.server:
                        self.xticks += event.xticks
                event_name = event.event_config.name
            self.yticks_label.append('%s(%s.%s)' % (event_name, key[1], key[2]))   # trace_id(server.core)

    def printevents(self):
        for i, event in enumerate(self.event_list):
            print('Event %d:\n%s\n' % (i, str(event)))

    def draw(self, pic):
        pic.set_events(self)
        pic.init_axes(self.time_range[0], self.time_range[1], 0, self.total_lines)
        for event in self.draw_event_list:
            event.draw(pic)
        pic.show(self.xticks, self.yticks_label)

    def find_event(self, x, y):
        if x is None or y is None: return None
        if not self.current_event is None:
            if self.current_event.is_in_rect_region(x, y):
                return self.current_event
            self.current_event.out_focus()
        for event in self.draw_event_list:
            if event.is_in_rect_region(x, y):
                event.on_focus()
                self.current_event = event
                return self.current_event
        self.current_event = None
        return self.current_event

    def on_dblclick(self, point):
        if self.current_event:
            self.current_event.on_dblclick()

class Parser:
    def __init__(self):
        self.parser_re = re.compile(r'\s*(-[\d\.]+) \[LTE:HLC (\d):(\d+)\.(\d+)\] (\w+)(.*)$')
        self.events = Events()

    def parse(self, filename):
        self.events.reset()
        with open(filename, 'r') as f:
            for line in f:
                trace = self.parse_line(line)
                if not trace is None:
                    self.events.add_trace(trace)
        self.events.statistics()
        return self.events

    def parse_line(self, line):
        #    -39126.18 [LTE:HLC 0:6.17] NR_L0_DLSRP_DL_FFT_TIMEBASE..................................... Numero: 1, RxStreamIdx: 1, Cp: 0, Lfn: 584, SubFrame: 6, Slot: 0, Symbol: 5
        #    -39125.20 [LTE:HLC 0:6.11] NR_L0_RADIO_PROC_FFT_COMPUTE_END
        r = self.parser_re.search(line)
        if r:
            time, hwi, server, core, id, params_text = float(r.group(1)), int(r.group(2)), int(r.group(3)), int(r.group(4)), r.group(5), r.group(6)
            trace_id = Trace.is_valid_id(id, params_text)
            if trace_id:
                trace = Trace(time, hwi, server, core, trace_id, params_text, line.strip())
                return trace
        return None

    def extract_files(self, filename):
        fpath, fext = os.path.splitext(filename)
        server_file_handles = {}
        files_write = []
        with open(filename, 'r') as f:
            for line in f:
                result = self.parse_line(line)
                if not result is None:
                    server = result['server']
                    if not server in server_file_handles:
                        file_write = '%s_server%d%s' % (fpath, server, fext)
                        files_write.append(file_write)
                        server_file_handles[server] = open(file_write, 'w')
                    server_file_handles[server].write(line)
                elif line.strip():
                    print('warning: line not in pattern: %s' % line.strip())
        for d, f in server_file_handles.items():
            f.close()
        return files_write

class TraceAnalyzer:
    def __init__(self):
        self.parser = Parser()
        self.pic = Pic()
        self.in_draw_line = False

    def draw(self, trace_file):
        #profile_start_time = time.time()
        if not os.path.isfile(trace_file): raise('file %s not found!' % trace_file)
        events = self.parser.parse(trace_file)
        #print('Parser Consuming: %.3fs' % (time.time() - profile_start_time))
        events.draw(self.pic)

class Key:
    pick_event_left_key = 'shift'
    pick_event_right_key = 'alt'
    pick_event_any_key = 'control'

class Pic:
    def __init__(self):
        self.fig = plt.figure('%s' % VERSION)
        self.ax = self.fig.add_subplot(111)
        self.in_draw_line = False
        self.current_event_rect = None
        self.line = None
        self.key_hold = {}
        for key in [Key.pick_event_left_key, Key.pick_event_right_key, Key.pick_event_any_key]:
            self.key_hold[key] = False

    def init_axes(self, x_min, x_max, y_min, y_max):
        self.x_min, self.x_max, self.y_min, self.y_max = x_min, x_max, y_min, y_max
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)

    def set_events(self, events):
        self.events = events

    def flush(self):
        self.fig.canvas.draw_idle()

    def on_mouse_move(self, event):
        if not event.xdata or not event.ydata: return
        is_flush = self.move_draw_line((event.xdata, event.ydata))
        event = self.events.find_event(event.xdata, event.ydata)
        if is_flush: self.flush()

    def move_draw_line(self, point):
        if self.in_draw_line:
            xdata, ydata = (self.line_start_point[0], point[0]), (self.line_start_point[1], point[1])
            if not self.line:
                self.line = plt.plot(xdata, ydata, 'ro-')
                self.line_text = self.ax.text(self.line_start_point[0], self.line_start_point[1] + 0.3, '', fontsize = 11, color = 'r')
            else:
                self.line[0].set_xdata(xdata)
                self.line[0].set_ydata(ydata)
            x_gap = point[0] - self.line_start_point[0]
            self.line_text.set_text('%.1fus' % x_gap)
            return True
        return False

    def click_draw_line(self, point, button):
        # button: 1 - left, 2 - middle, 3 - right
        if self.in_draw_line:
            if self.line:
                pick_point = self.pick_point(point, must_hold_key = False)
                if not pick_point: return
                self.move_draw_line(pick_point)
                if button == 3:
                    self.line[0].remove()
                    self.line_text.remove()
                self.line = None
                self.flush()
            self.in_draw_line = False
        else:
            if button != 1: return
            pick_point = self.pick_point(point)
            if pick_point:
                self.in_draw_line = True
                self.line_start_point = pick_point
                self.move_draw_line(point)
                self.flush()

    def on_mouse_click(self, event):
        if not event.xdata or not event.ydata: return
        self.click_draw_line((event.xdata, event.ydata), event.button)
        if event.dblclick: self.events.on_dblclick((event.xdata, event.ydata))

    def on_key_press(self, event):
        #print('press %s' % event.key)
        self.key_hold[event.key] = True

    def on_key_release(self, event):
        self.key_hold[event.key] = False

    def pick_point(self, point, must_hold_key = True):
        if self.key_hold[Key.pick_event_any_key]:
            return point
        elif self.key_hold[Key.pick_event_left_key] or self.key_hold[Key.pick_event_right_key]:
            event = self.events.find_event(point[0], point[1])
            if event:
                if self.key_hold[Key.pick_event_left_key]:
                    point = (event.rect_region[0], (event.rect_region[2] + event.rect_region[3])/2)
                else:
                    point = (event.rect_region[1], (event.rect_region[2] + event.rect_region[3])/2)
                return point
        elif not must_hold_key:
            return point
        return None

    def show(self, xticks, yticks_label):
        self.fig.canvas.mpl_connect('button_press_event', self.on_mouse_click)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)
        self.fig.canvas.mpl_connect('key_release_event', self.on_key_release)
        plt.xticks(xticks)
        plt.yticks(range(len(yticks_label)), yticks_label[::-1])
        plt.grid(axis = 'both', linestyle = '--')
        plt.subplots_adjust(bottom = 0.05, right = 0.95)
        self.event_text = self.ax.text(-0.1, 1.02, '', fontsize = 10, color = 'red', transform = self.ax.transAxes)
        plt.show()

    def draw_rect(self, rect_region, color = 'b'):
        (x_start, x_end, y_start, y_end) = rect_region
        rect = patches.Rectangle((x_start, y_start), x_end - x_start, y_end - y_start, color = color)
        self.ax.add_patch(rect)

VERSION = 'Trace Analyzer v0.2, 20210205'

if __name__ == '__main__':
    #test_trace_file = 'trace_1_server6_test.txt'
    #test_trace_file = 'trace_1_server6.txt'
    test_trace_file = 'trace_1.txt'
    trace_file = sys.argv[1] if len(sys.argv) > 1 else test_trace_file
    config_file = sys.argv[2] if len(sys.argv) > 2 else ''
    trace_config = None
    if config_file and os.path.isfile(config_file):
        trace_config = __import__(os.path.splitext(os.path.basename(config_file))[0])
    g_events_config = EventsConfig(trace_config)
    trace_analyzer = TraceAnalyzer()
    trace_analyzer.draw(trace_file)

