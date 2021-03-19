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
# 'filter': only the trace id with the filtered content will be considered as this trace, filter should be a tuple if there's start trace and end trace. The filter applied is a regular expression.
#
# Notes:
# 'combine_core' and 'rand_core_color' are applied to an event (trace groups), it should be set to the first trace of an event
# other options are applied to each trace, it should be set to each trace
#
################################################################################################################################################################################################

context_searcher_show = False
context_radio_show    = False
context_dlsrp_show    = False
context_dlctrl_show   = False
context_pdschbrp_show = False
context_ulctrl_show   = False
context_ulsrp_show    = False

context_searcher_core  = False
context_radio_core     = True
context_dlsrp_core     = False
context_dlctrl_core    = False
context_pdschbrp_core  = False
context_ulctrl_core    = False
context_ulsrp_core     = True

keypath_searcher_show = True
keypath_radio_show    = True
keypath_dlsrp_show    = True
keypath_dlctrl_show   = True
keypath_pdschbrp_show = True
keypath_ulctrl_show   = True
keypath_ulsrp_show    = True

keypath_searcher_core  = False
keypath_radio_core     = True
keypath_dlsrp_core     = True
keypath_dlctrl_core    = False
keypath_pdschbrp_core  = False
keypath_ulctrl_core    = True
keypath_ulsrp_core     = True

detailpath_searcher_show = False
detailpath_radio_show    = False
detailpath_dlsrp_show    = True
detailpath_dlctrl_show   = False
detailpath_pdschbrp_show = True
detailpath_ulctrl_show   = False
detailpath_ulsrp_show    = False

detailpath_searcher_core  = True
detailpath_radio_core     = True
detailpath_dlsrp_core     = False
detailpath_dlctrl_core  = True
detailpath_pdschbrp_core  = False
detailpath_ulctrl_core    = True
detailpath_ulsrp_core     = True

TRACES_CONFIG = {
    'RADIO PROC': [(1, 'RADIO_DCL2', [(('NR_L0_RADIO_PROC_OFFLOADING_START', 'NR_L0_RADIO_PROC_OFFLOADING_END'), 'c', {'combine_core': keypath_radio_core,'show': keypath_radio_show})]),
                   (2, 'RADIO_STREAM', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'darkred', {'combine_core': context_radio_core,'show': context_radio_show, 'filter': ('Next Task: NRL0RPROC_STREAM_H.I.T._NR', 'Prev Task: NRL0RPROC_STREAM_H.I.T._NR')}),
                   (('NR_L0_RADIO_PROC_START', 'NR_L0_RADIO_PROC_END'), 'c', {'combine_core': keypath_radio_core,'show': keypath_radio_show}),
                   ('NR_L0_RADIO_PROC_SEND_FFT_IND', 'r', {'filter': 'Sym: 0','combine_core': keypath_radio_core, 'show': keypath_radio_show})]),
                 ],
    'DLSRP': [ 
               (10, 'DLSRP_FFT_DATA', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'darkred', {'combine_core': context_dlsrp_core,'show': context_dlsrp_show, 'filter': ('Next Task: NRL0DLSRP_FFT_DATA_H.I.T._NR', 'Prev Task: NRL0DLSRP_FFT_DATA_H.I.T._NR')}),
                                       (('NR_L0_DLSRP_DL_FFT_DATA_START', 'NR_L0_DLSRP_DL_FFT_DATA_END'), 'c', {'combine_core': keypath_dlsrp_core|context_dlsrp_core,'show': keypath_dlsrp_show|context_dlsrp_show}),
                                       #('NR_L0_DLSRP_DL_FFT_TIMEBASE', 'b', {'combine_core': keypath_dlsrp_core|context_dlsrp_core, 'show': keypath_dlsrp_show|context_dlsrp_show, 'filter': 'RxStreamIdx: 0,.*,Symbol: 0'}),
                                       #('NR_L0_DLSRP_DL_FFT_TIMEBASE', 'b', {'combine_core': keypath_dlsrp_core|context_dlsrp_core, 'show': keypath_dlsrp_show|context_dlsrp_show, 'filter': 'RxStreamIdx: 0,.*,Symbol: 1$'}),
                                       ('NR_L0_DLSRP_TIMING_SUBFRAME', 'brown', {'combine_core': keypath_dlsrp_core|context_dlsrp_core, 'show': keypath_dlsrp_show|context_dlsrp_show,'xtick': True}),
                                       ('FRAMEWORK_MSG_Q_SEND', 'orange', {'filter': 'NR_L0_DLSRP_PDCCH_DEMOD_IND','combine_core': keypath_dlsrp_core, 'show': keypath_dlsrp_show})]),
                                  
               (11, 'DLSRP_PDCCH', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'darkred', {'combine_core': context_dlsrp_core,'show': context_dlsrp_show, 'filter': ('Next Task: NRL0DLSRP_PDCCH_H.I.T._NR', 'Prev Task: NRL0DLSRP_PDCCH_H.I.T._NR')}),
                                    (('NR_L0_DLSRP_PDCCH_START', 'NR_L0_DLSRP_PDCCH_END'), 'c', {'combine_core': keypath_dlsrp_core, 'show': keypath_dlsrp_show}),
                                    ('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0_DLC_PDCCH_DATA_SYMS_IND','combine_core': keypath_dlsrp_core, 'show': keypath_dlsrp_show})]),
               
               (12, 'DLSRP_PDSCH_CTRL', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_dlsrp_core,'show': context_dlsrp_show, 'filter': ('Next Task: NRL0DLSRP_CFG_NR', 'Prev Task: NRL0DLSRP_CFG_NR')}),
                                         (('NR_L0_DLSRP_PDSCH_INFO_START', 'NR_L0_DLSRP_PDSCH_INFO_END'), 'c', {'combine_core': detailpath_dlsrp_core, 'show': detailpath_dlsrp_show})]),
               
               (13, 'DLSRP_PDSCH', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_dlsrp_core,'show': context_dlsrp_show, 'filter': ('Next Task: NRL0DLSRP_PDSCH_H.I.T._NR', 'Prev Task: NRL0DLSRP_PDSCH_H.I.T._NR')}),
                                    (('NR_L0_DLSRP_PDSCH_PART_1_START', 'NR_L0_DLSRP_PDSCH_PART_1_END'), 'c', {'combine_core': detailpath_dlsrp_core,'show': detailpath_dlsrp_show}),
                                    (('NR_L0_DLSRP_PDSCH_PART_2_START', 'NR_L0_DLSRP_PDSCH_PART_2_END'), 'c', {'combine_core': detailpath_dlsrp_core,'show': detailpath_dlsrp_show}),
                                    ('NR_L0_DLSRP_SEND_SD_MSG', 'r', {'combine_core': detailpath_dlsrp_core, 'show': detailpath_dlsrp_show})]),
                                                         
               (14, 'DlSRP_PBCH', [(('NR_L0_DLSRP_PBCH_START', 'NR_L0_DLSRP_PBCH_END'), 'c', {'combine_core': detailpath_dlsrp_core, 'show': detailpath_dlsrp_show})]), 
              ],
    'DLCTRL': [
               (20, 'DLCTRL_PDCCHBRP', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'darkred', {'combine_core': context_dlctrl_core,'show': context_dlctrl_show, 'filter': ('Next Task: NRL0DLCTRL_PDCCH_BRP_H.I._NR', 'Prev Task: NRL0DLCTRL_PDCCH_BRP_H.I._NR')}),
                                        (('NR_L0_DLC_PDCCH_BRP_START', 'NR_L0_DLC_PDCCH_BRP_SD_END'), 'c', {'combine_core': keypath_dlctrl_core, 'show': keypath_dlctrl_show})]),
               
               (21, 'PDCCH Coprocessor', [(('NR_L0_DLC_COPRO_DECODE_START', 'NR_L0_DLC_COPRO_DECODE_END'), 'c', {'filter': ('','LastCnf: True'), 'same_core': False, 'combine_core': keypath_dlctrl_core, 'show': keypath_dlctrl_show})]),                         
               
               (22, 'DLCTRL_PDCCHBRP_TASK', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'darkred', {'combine_core': context_dlctrl_core,'show': context_dlctrl_show, 'filter': ('Next Task: NRL0DLCTRL_PDCCH_BRP_H.I.T._NR', 'Prev Task: NRL0DLCTRL_PDCCH_BRP_H.I.T._NR')}),
                                             (('NR_L0_DLC_COPRO_CNF_TASK_START', 'NR_L0_DLC_COPRO_CNF_TASK_END'), 'c', {'combine_core': keypath_dlctrl_core, 'show': keypath_dlctrl_show})]),
               
               (23, 'DLCTRL_PDCCHBRP_RSLT', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'darkred', {'combine_core': context_dlctrl_core,'show': context_dlctrl_show, 'filter': ('Next Task: NRL0DLCTRL_PDCCH_BRP_RSLT_H.I._NR', 'Prev Task: NRL0DLCTRL_PDCCH_BRP_RSLT_H.I._NR')}),
                                             (('NR_L0_DLC_SD_TASK_RSLT_START', 'NR_L0_DLC_SD_TASK_RSLT_END'), 'c', {'combine_core': keypath_dlctrl_core, 'show': keypath_dlctrl_show}),
                                             ('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0L1_PHY_DLC_UL_SCH_DATA_READY_IND','combine_core': keypath_dlctrl_core, 'show': keypath_dlctrl_show}),
                                             ('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0_DLSRP_PDCCH_INFO_IND','combine_core': keypath_dlctrl_core, 'show': keypath_dlctrl_show}),
                                             ('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0_PDSCHBRP_DLC_DECODE_INFO_IND','combine_core': keypath_dlctrl_core, 'show': keypath_dlctrl_show})]),
                                             
               (24, 'DLCTRL_PBCHBRP', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_dlctrl_core,'show': context_dlctrl_show, 'filter': ('Next Task: NRL0DLCTRL_PBCH_BRP_H.I._NR', 'Prev Task: NRL0DLCTRL_PBCH_BRP_H.I._NR')})]),
               (25, 'DLCTRL_HARQCTRL', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_dlctrl_core,'show': context_dlctrl_show, 'filter': ('Next Task: DLCTRL_HARQ_CTRL_H.I._NR', 'Prev Task: DLCTRL_HARQ_CTRL_H.I._NR')}),
                                        ('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0L1_PHY_DLC_PDSCH_CTRL_IND','combine_core': keypath_dlctrl_core,'show': keypath_dlctrl_show}),
                                        ('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0_ULC_DLC_SEND_HARQ_IND','combine_core': keypath_dlctrl_core,'show': keypath_dlctrl_show})]),             
               ],
             
    'PDSCH BRP': [
                  (30, 'PDSCHBRP_CTRL', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_pdschbrp_core,'show': context_pdschbrp_show, 'filter': ('Next Task: NRL0PDSCHBRP_CTRL_H.I._NR', 'Prev Task: NRL0PDSCHBRP_CTRL_H.I._NR')}),
                                         (('NR_L0_PDSCHBRP_CTRL_IND_START', 'NR_L0_PDSCHBRP_CTRL_IND_END'), 'c', {'combine_core': detailpath_pdschbrp_core,'show': detailpath_pdschbrp_show})]),
                                         
                  (31, 'PDSCHBRP_DATA', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_pdschbrp_core,'show': context_pdschbrp_show, 'filter': ('Next Task: NRL0PDSCHBRP_DATA_H.I._NR', 'Prev Task: NRL0PDSCHBRP_DATA_H.I._NR')}),
                                         (('NR_L0_PDSCHBRP_DATA_IND_START', 'NR_L0_PDSCHBRP_DATA_IND_END'), 'c', {'combine_core': detailpath_pdschbrp_core,'show': detailpath_pdschbrp_show})]),
                  
                  (32, 'PDSCHBRP_COPRO_IND', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_pdschbrp_core,'show': context_pdschbrp_show, 'filter': ('Next Task: NRL0PDSCHBRP_COPRO_IND_H.I.T._N', 'Prev Task: NRL0PDSCHBRP_COPRO_IND_H.I.T._N')}),
                                              (('NR_L0_PDSCHBRP_COPRO_REQ_START', 'NR_L0_PDSCHBRP_COPRO_REQ_END'), 'c', {'combine_core': detailpath_pdschbrp_core,'show': detailpath_pdschbrp_show})]),
                      
                  (33, 'PDSCHBRP Copro CNF DCL2', [(('NR_L0_PDSCHBRP_COPRO_CNF_START', 'NR_L0_PDSCHBRP_COPRO_CNF_END'), 'c', {'combine_core': True,'show': context_pdschbrp_show|detailpath_pdschbrp_show}),
                                                    #('FPGACARD_RECV', 'b', {'filter': 'Card: 0, Window: 0','combine_core': context_pdschbrp_core|detailpath_pdschbrp_core,'show': context_pdschbrp_show|detailpath_pdschbrp_show}),
                                                    ('NR_L0_PDSCHBRP_PHY_IND', 'r', {'combine_core': True,'show': context_pdschbrp_show|detailpath_pdschbrp_show}), # ('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0L1_PHY_BRP_PDSCH_DATA_IND','combine_core': True})
                                                    ('NR_L0_PDSCHBRP_CRC_IND', 'r', {'combine_core': True,'show': context_pdschbrp_show|detailpath_pdschbrp_show})]), # ('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_DLC_PDSCHBRP_CRC_RESULTS_IND','combine_core': True})                                          
                 ],
                 
    'UL CTRL': [(40, 'ULCTRL_CTRL', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_ulctrl_core,'show': context_ulctrl_show, 'filter': ('Next Task: NRL0ULCTRL_CTRL_H.I._NR', 'Prev Task: NRL0ULCTRL_CTRL_H.I._NR')}),
                                     (('NR_L0_ULC_SCHEDULE_TTI_START', 'NR_L0_ULC_SCHEDULE_TTI_END'), 'c', {'combine_core': keypath_ulctrl_core,'show': keypath_ulctrl_show}),
                                     (('NR_L0_ULC_DPHY_DATA_READY_RSP_RECEIVED'), 'b', {'combine_core': keypath_ulctrl_core,'show': keypath_ulctrl_show}),
                                     (('NR_L0_ULC_PUSCH_SCHEDULING_START', 'NR_L0_ULC_PUSCH_SCHEDULING_END'), 'c', {'combine_core': detailpath_ulctrl_core,'show': detailpath_ulctrl_show}),
                                     ('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0_ULC__PUSCH_ENCODE_MSG','combine_core': detailpath_ulctrl_core,'show': detailpath_ulctrl_show}),
                                     (('NR_L0_ULC_PUCCH_SCHEDULING_START', 'NR_L0_ULC_PUCCH_SCHEDULING_END'), 'c', {'combine_core': detailpath_ulctrl_core,'show': detailpath_ulctrl_show}),
                                      ('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0_ULC__PUCCH_ENCODE_MSG','combine_core': detailpath_ulctrl_core,'show': detailpath_ulctrl_show}),
                                     (('NR_L0_ULC_SRS_SCHEDULING_START', 'NR_L0_ULC_SRS_SCHEDULING_END'), 'c', {'combine_core': detailpath_ulctrl_core,'show': detailpath_ulctrl_show})]),                        
               ],
               
    'UL BRP':  [ (50, 'ULCTRL_HARQ_ENC', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_ulctrl_core|keypath_ulctrl_core,'show': context_ulctrl_show|keypath_ulctrl_show, 'filter': ('Next Task: NRL0ULCTRL_HARQ_ENC_H.I._NR', 'Prev Task: NRL0ULCTRL_HARQ_ENC_H.I._NR')}),
                                           ('FRAMEWORK_MSG_RECV', 'r', {'filter': 'NR_L0_ULC_DLC_SEND_HARQ_IND','combine_core': keypath_ulctrl_core,'show': keypath_ulctrl_show})]),
                 
                 (51, 'ULCTRL_PUSCH_ENC', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_ulctrl_core|keypath_ulctrl_core,'show': context_ulctrl_show|keypath_ulctrl_show, 'filter': ('Next Task: NRL0ULCTRL_PUSCH_ENC_H.I._NR', 'Prev Task: NRL0ULCTRL_PUSCH_ENC_H.I._NR')}),
                                           ('NR_L0_ULBRP_UCP_REQ_MSG_SENT', 'r', {'combine_core': keypath_ulctrl_core,'show': keypath_ulctrl_show}),                                            
                                           ('NR_L0_ULBRP_UCP_HARQ_REQ_MSG_SENT', 'r', {'combine_core': keypath_ulctrl_core,'show': keypath_ulctrl_show}),
                                           ('NR_L0_ULBRP_UCP_CSI_REQ_MSG_SENT', 'r', {'combine_core': keypath_ulctrl_core,'show': keypath_ulctrl_show}),
                                           ('NR_L0_ULBRP_ULC_CONFIG_MSG_RECEIVED', 'b', {'combine_core': keypath_ulctrl_core,'show': keypath_ulctrl_show}),
                                           ('NR_L0_ULBRP_MAC_PAYLOAD_MSG_RECEIVED', 'b', {'combine_core': keypath_ulctrl_core,'show': keypath_ulctrl_show})]),
                                           
                 (53, 'ULCTRL_PUCCH_ENC', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_ulctrl_core|keypath_ulctrl_core,'show': context_ulctrl_show|keypath_ulctrl_show, 'filter': ('Next Task: NRL0ULCTRL_PUCCH_ENC_H.I._NR', 'Prev Task: NRL0ULCTRL_PUCCH_ENC_H.I._NR')}),
                                           (('NR_L0_ULBRP_UCP_PUCCH_REQ_MSG_SENT'), 'r', {'same_core': keypath_ulctrl_core, 'combine_core': keypath_ulctrl_core,'show': keypath_ulctrl_show})]),
                             
                 
                 (52, 'ULBRP PUSCH encode CNF DCL2', [('NR_L0_ULBRP_UCP_RSP_MSG_RECEIVED', 'b', {'same_core': keypath_ulctrl_core, 'combine_core': keypath_ulctrl_show,'show': keypath_ulctrl_show}),
                                                      ('NR_L0_ULBRP_SEND_MAP_PUSCH_DATA_MSG', 'r', {'combine_core': keypath_ulctrl_core,'show': keypath_ulctrl_show})]),
                                             
                 (54, 'ULBRP PUCCH encode CNF DLC2', [('NR_L0_ULBRP_UCP_PUCCH_RSP_MSG_RECEIVED', 'b', {'same_core': keypath_ulctrl_core, 'combine_core': keypath_ulctrl_show,'show': keypath_ulctrl_show}),
                                                      ('NR_L0_ULBRP_SEND_MAP_PUCCH_DATA_MSG', 'r', {'combine_core': keypath_ulctrl_core,'show': keypath_ulctrl_show})]),                              
               ],
               
     'UL SRP': [ (60, 'ULSRP_PRACH', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_ulsrp_core,'show': context_ulsrp_show, 'filter': ('Next Task: NRL0ULSRP_PRACH_H.I._NR', 'Prev Task: NRL0ULSRP_PRACH_H.I._NR')})]),
                 (61, 'ULSRP_SRS', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'grey', {'combine_core': context_ulsrp_core|keypath_ulsrp_core,'show': context_ulsrp_show|keypath_ulsrp_show, 'filter': ('Next Task: NRL0ULSRP_SRS_H.I._NR', 'Prev Task: NRL0ULSRP_SRS_H.I._NR')}),
                                   (('NR_L0_ULSRP_SRS_CONFIG_RECEIVED'), 'b', {'combine_core': keypath_ulsrp_core,'show': keypath_ulsrp_show})]),
                 (62, 'ULSRP_MAPPING', [(('HLC_CONTEXT_SWITCH', 'HLC_CONTEXT_SWITCH'), 'darkred', {'combine_core': context_ulsrp_core,'show': context_ulsrp_show, 'filter': ('Next Task: NRL0ULSRP_MAPPING_H.I.T._NR', 'Prev Task: NRL0ULSRP_MAPPING_H.I.T._NR')}),
                                        (('NR_L0_ULSRP_PUSCH_MAPPING_START', 'NR_L0_ULSRP_PUSCH_MAPPING_END'), 'c', {'combine_core': keypath_ulsrp_core,'show': keypath_ulsrp_show}),
                                        (('NR_L0_ULSRP_PUCCH_MAPPING_START', 'NR_L0_ULSRP_PUCCH_MAPPING_END'), 'darkcyan', {'combine_core': keypath_ulsrp_core,'show': keypath_ulsrp_show}),
                                        (('NR_L0_ULSRP_SRS_MAPPING_START', 'NR_L0_ULSRP_SRS_MAPPING_END'), 'springgreen', {'combine_core': keypath_ulsrp_core,'show': keypath_ulsrp_show})]),
                 (63, 'UlSrp Tick', [(('NR_L0_ULSRP_TICK_HANDLING_START', 'NR_L0_ULSRP_TICK_HANDLING_END'), 'lime', {'combine_core': keypath_ulsrp_core,'show': keypath_ulsrp_show}),
                                     ('NR_L0_ULSRP_TIMING_SLOT', 'brown', {'combine_core': context_ulsrp_core|keypath_ulsrp_core,'show': context_ulsrp_show|keypath_ulsrp_show})]),
               ],
              }

