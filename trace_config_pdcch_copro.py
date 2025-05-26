#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################################################################################################################################
#
# TRACES_CONFIG:
#
# component: [(priority, event name, [((start_trace_id, end_trace_id), color, {'combine_core': True, 'rand_core_color': True, 'same_core': False, 'show': False, 'xtick': True, 'filter': '...'}),
#                                      (trace_id, color, {options}),
#                                      (trace_id, color, {options})]),
#             (priority, event name, [...]),
#             ]
#
# priority: the show order from top to bottom is the priority number from small to big
#
# color: 'k', 'grey', 'brown', 'darkred', 'r', 'orange', 'gold', 'y', 'yellowgreen', 'g', 'lime', springgreen', 'c', 'darkcyan',
#        'skyblue', 'steelblue', 'navy', 'b', 'violet', 'purple', 'm', 'pink', 'deeppink'
#        color can be a list of colors, the first color will be used for the first trace, the second color for the second trace, and so on.
#
# options:
# 'combine_core': show different cores on the same line, default: False
# 'rand_core_color': when different cores on the same line, show different cores traces with different random color, default: False
# 'same_core': start trace and end trace can be on different cores or not, default: False
# 'show': show this trace or not, default: True
# 'xtick': show a xtick line with this trace, default: False
# 'filter': only the trace id with the filtered content will be considered as this trace, filter should be a tuple if there's start trace and end trace. The filter applied is a regular expression.
#
# Notes:
# 'combine_core' and 'rand_core_color' are applied to an event (trace groups), it should be set to the first trace of an event
# other options are applied to each trace, it should be set to each trace
#
################################################################################################################################################################################################

TRACES_CONFIG = {
    'RADIO PROC': [(1, 'Offloading', [(('NR_L0_RADIO_PROC_OFFLOADING_START', 'NR_L0_RADIO_PROC_OFFLOADING_END'), ['r', 'g', 'b'], {'show': False})]),
                   (2, 'RadioProc', [(('NR_L0_RADIO_PROC_START', 'NR_L0_RADIO_PROC_END'), ['r', 'g', 'b'], {})]),
                  ],
    'DL SRP': [(9, 'Symbol', [('NR_L0_DLSRP_TIMING_SYM', ['r', 'g', 'b'], {'xtick': True})]),
               (10, 'FFT', [(('NR_L0_DLSRP_DL_FFT_DATA_START', 'NR_L0_DLSRP_DL_FFT_DATA_END'), ['r', 'g', 'b'], {})]),
               (11, '->DlCtrl', [('FRAMEWORK_MSG_SEND', 'g', {'filter': 'NR_L0_DLC_PDCCH_DATA_SYMS_IND'})]),
               (12, 'Pdcch', [(('NR_L0_DLSRP_PDCCH_START', 'NR_L0_DLSRP_PDCCH_END'), ['m', 'darkred'], {})]),
               (13, 'Pdcch Est', [(('NR_L0_DLSRP_PDCCH_CHAN_EST_START', 'NR_L0_DLSRP_PDCCH_CHAN_EST_END'), ['r', 'g', 'b'], {})]),
               (14, 'Pdcch Est Coeff', [(('NR_L0_DLSRP_PDCCH_EQ_COEFF_START', 'NR_L0_DLSRP_PDCCH_EQ_COEFF_END'), ['r', 'g', 'b'], {})]),
               (15, 'Pdcch EQ', [(('NR_L0_DLSRP_PDCCH_EQUALIZE_START', 'NR_L0_DLSRP_PDCCH_EQUALIZE_END'), ['r', 'g', 'b'], {})]),
               (16, 'Pdcch Demap', [(('NR_L0_DLSRP_PDCCH_DEMAP_START', 'NR_L0_DLSRP_PDCCH_DEMAP_END'), ['r', 'g', 'b'], {})]),
               (17, 'REQD Create', [('NR_L0_DLSRP_PDCCH_COPRO_REQD_CREATE', ['r', 'g', 'b'], {})]),
               (18, 'REQD Send', [('NR_L0_DLSRP_PDCCH_COPRO_REQD_SEND', ['r', 'g', 'b'], {})]),
              ],
    'DL CTRL': [(20, 'REQC Process', [(('NR_L0_DLC_PDCCH_BRP_START', 'NR_L0_DLC_PDCCH_BRP_SD_END'), ['r', 'g', 'b'], {})]),
              #(21, 'REQC Process', [(('NR_L0_DLC_PDCCH_BRP_COPRO_REQ_START', 'NR_L0_DLC_PDCCH_BRP_COPRO_REQ_END'), ['r', 'g', 'b'], {})]),
              (22, 'REQC Send', [('NR_L0_DLC_COPRO_DECODE_START', ['r', 'g', 'b'], {})]),
              #(23, 'Pdcch Copro end', [('NR_L0_DLC_COPRO_DECODE_END', ['r', 'g', 'b'], {})]),
              (24, 'Pdcch Copro Cnf', [(('NR_L0_DLC_COPRO_CNF_TASK_START', 'NR_L0_DLC_COPRO_CNF_TASK_END'), ['r', 'g', 'b'], {})]),
              (25, 'Pdcch Sd Result', [(('NR_L0_DLC_SD_TASK_RSLT_START', 'NR_L0_DLC_SD_TASK_RSLT_END'), ['r', 'g', 'b'], {}),
                                       ('FRAMEWORK_MSG_SEND', 'm', {'filter': 'NR_L0L1_PHY_DLC_UL_SCH_DATA_READY_IND'})]),
             ],
}

