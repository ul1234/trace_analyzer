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
    'DL SRP': [(10, 'DlSrp FFT', [(('NR_L0_DLSRP_DL_FFT_DATA_START', 'NR_L0_DLSRP_DL_FFT_DATA_END'), 'r', {'show': False})]),
               (11, 'DlSrp Pdcch', [(('NR_L0_DLSRP_PDCCH_START', 'NR_L0_DLSRP_PDCCH_END'), 'm', {'xtick': True})]),
              ],
    'PDCCH': [(20, 'Pdcch Brp', [(('NR_L0_DLC_PDCCH_BRP_START', 'NR_L0_DLC_PDCCH_BRP_SD_END'), 'k', {})]),
              (23, 'MSG to L1', [('FRAMEWORK_MSG_SEND', 'g', {'filter': 'NR_L0L1_PHY_DLC_UL_SCH_DATA_READY_IND', 'combine_core': True, 'rand_core_color': True}),
                                 ('FRAMEWORK_MSG_SEND', 'b', {'filter': 'NR_L0L1_PHY_DLC_PDSCH_CTRL_IND', 'combine_core': True, 'rand_core_color': True}),
                                 ('FRAMEWORK_MSG_SEND', 'm', {'filter': 'NR_L0L1_PHY_BRP_PDSCH_DATA_IND', 'combine_core': True, 'rand_core_color': True})]),
             ],
    'PDSCH BRP': [(35, 'HARQ Msg', [('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0_ULC_DLC_SEND_HARQ_IND'})]),
                 ],
    'UL CTRL': [(40, 'UlCtrl Tti', [(('NR_L0_ULC_SCHEDULE_TTI_START', 'NR_L0_ULC_SCHEDULE_TTI_END'), 'c', {'show': False})]),
               ],
    'MAC': [(80, 'L1 UL PHY', [(('NR_UL_L1_RX_PDCCH_PHY_IND_START', 'NR_UL_L1_RX_PDCCH_PHY_IND_END'), 'r', {})]),
            (81, 'L1 DL PHY', [('NR_L1_PHY_PDSCH_CTRL_IND', 'g', {})]),
           ]
              }

