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
#
# options:
# 'combine_core': show different cores on the same line, default: False
# 'rand_core_color': when different cores on the same line, show different cores traces with different random color, default: False
# 'same_core': start trace and end trace can be on different cores or not, default: False
# 'show': show this trace or not, default: True
# 'xtick': show a xtick line with this trace, default: False
# 'filter': only the trace id with the filtered content will be considered as this trace
#
# Notes:
# 'combine_core' and 'rand_core_color' are applied to an event (trace groups), it should be set to the first trace of an event
# other options are applied to each trace, it should be set to each trace
#
################################################################################################################################################################################################

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
                  (31, 'Pdsch Copro Req', [(('NR_L0_PDSCHBRP_COPRO_REQ_START', 'NR_L0_PDSCHBRP_COPRO_REQ_END'), 'g', {'combine_core': True, 'rand_core_color': True})]),
                  (32, 'Pdsch Copro Cnf', [(('NR_L0_PDSCHBRP_COPRO_CNF_START', 'NR_L0_PDSCHBRP_COPRO_CNF_END'), 'r', {'show': False})]),
                  (33, 'Pdsch Post', [(('NR_L0_PDSCHBRP_POST_PROCESS_START', 'NR_L0_PDSCHBRP_POST_PROCESS_END'), 'm', {}),
                                      ('NR_L0_PDSCHBRP_PHY_IND', 'r', {})]),
                  (34, 'Pdsch Msg', [('NR_L0_PDSCHBRP_PHY_IND_CRC_RESULTS', 'k', {'show': False})]),
                  (35, 'HARQ Msg', [('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0_ULC_DLC_SEND_HARQ_IND'}),
                                    ('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0L1_PHY_DLC_PDSCH_CTRL_IND'})]),
                  (36, 'Pdsch Param', [(('NR_L0_PDSCHBRP_PARAMS_UE_START', 'NR_L0_PDSCHBRP_PARAMS_CB_END'), 'gold', {}),
                                       ('NR_L0_PDSCHBRP_PARAMS_TB', 'm', {}),
                                       ('NR_L0_PDSCHBRP_PARAMS_CB_1', 'b', {'show': False}),
                                       ('NR_L0_PDSCHBRP_PARAMS_CB_2', 'g', {'show': False})]),
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

