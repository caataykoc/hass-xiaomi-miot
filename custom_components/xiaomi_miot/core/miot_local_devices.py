"""
1. https://new.cnzz.com/v1/login.php?siteid=1280294351
2. Login with password: hass-xiaomi-miot
3. https://web.umeng.com/main.php?c=eanalysis&a=frame&siteid=1280294351#!/0/eanalysis/category/3/1280294351/2021-01-01/0
4. Search model via https://home.miot-spec.com
"""

MIOT_LOCAL_MODELS = [
    '090615.curtain.kcz82d',
    '090615.curtain.ptx82',
    '090615.curtain.sidt82',
    '090615.curtain.ykgc82',
    'ateai.mosq.dakuo',
    'aupu.bhf_light.s368m',
    # 'babai.curtain.190812',  # mode/current_position return -4004
    # 'babai.curtain.bb82mj',  # mode/current_position return -4004
    # 'babai.curtain.m515e',   # mode/current_position return -4004
    # 'babai.curtain.mtx850',  # mode/current_position return -4004
    'babai.switch.bb101s',
    'babai.switch.bb102s',
    'babai.switch.bb103s',
    'babai.switch.th01a',
    'bj352.airp.y106cm',
    'bj352.waterpuri.k10',
    'careli.fryer.maf01',
    'careli.fryer.maf02',
    'careli.fryer.maf03',
    'cgllc.airm.cgdn1',
    'chuangmi.camera.026c02',
    'chuangmi.camera.039a01',
    'chuangmi.plug.212a01',
    'chunmi.health_pot.a1',
    'chunmi.ihcooker.slim',
    'chunmi.ihcooker.v2',
    'chunmi.microwave.n20l02',
    'chunmi.pre_cooker.dylg5',
    'chunmi.pre_cooker.mini1',
    'chunmi.waterpuri.600f2',
    'chunmi.waterpuri.600j6',
    'chunmi.waterpuri.800f3',
    'coc.dryer.fdpsm',
    # 'cubee.airrtc.th123e',  # issues/282
    # 'cubee.airrtc.th123w',  # issues/213
    'cuco.light.sl4',
    'cuco.plug.co1',
    'cuco.plug.cp1',
    'cuco.plug.cp1m',
    'cuco.plug.cp2',
    'cuco.plug.cp2a',
    'cuco.plug.cp3a',
    'cuco.plug.cp5pro',
    'cuco.plug.sp5',
    'deerma.humidifier.jsq3',
    'deerma.humidifier.jsq4',
    'deerma.humidifier.jsq5',
    'deerma.humidifier.jsqm',
    'deerma.humidifier.jsqs',
    'deerma.humidifier.rz300',
    'deye.derh.u20a3',
    'dmaker.airp.swift',
    'dmaker.airpurifier.f20',
    'dmaker.fan.1c',
    'dmaker.fan.1e',
    'dmaker.fan.p10',
    'dmaker.fan.p11',
    'dmaker.fan.p15',
    'dmaker.fan.p18',
    'dmaker.fan.p8',
    'dmaker.fan.p9',
    'dooya.curtain.c1',
    'dooya.curtain.m1',
    'dooya.curtain.m2',
    'dooya.curtain.m5',
    'dreame.vacuum.mb1808',
    'dreame.vacuum.mc1808',
    'dreame.vacuum.p2008',
    'dreame.vacuum.p2009',
    'dreame.vacuum.p2027',
    'dreame.vacuum.p2028',
    'dreame.vacuum.p2029',
    'dreame.vacuum.p2036',
    'dreame.vacuum.p2041',
    'dreame.vacuum.p2041o',
    'dreame.vacuum.p2140',
    'dreame.vacuum.p2148o',
    'dreame.vacuum.p2149o',
    'dreame.vacuum.p2150b',
    'dreame.vacuum.p2150o',
    'dreame.vacuum.p2157',
    'dreame.vacuum.p2187',
    'dreame.vacuum.p2259',
    'fawad.airrtc.30011',
    'fawad.airrtc.30012',
    'fengmi.projector.l176',
    'fengmi.projector.l176jp',
    'fengmi.projector.l185',
    'fengmi.projector.l206j',
    'fengmi.projector.m045j',
    'fengmi.projector.m085j',
    'fengmi.projector.m135jp',
    'galime.curtain.gp72',
    'gerwin.curtain.gm25xm',
    'hddz.blanket.zndrt',
    'hfjh.fishbowl.v2',
    'huayi.light.fanwy',
    'hyd.airer.znlyj1',
    'hyd.airer.znlyj3',
    'hyd.airer.znlyj4',
    'ijai.vacuum.v1',
    'ijai.vacuum.v10',
    'ijai.vacuum.v13',
    'ijai.vacuum.v14',
    'ijai.vacuum.v2',
    'ijai.vacuum.v3',
    'isa.camera.hlc7',
    'isleep.blanket.hs2001',
    'isleep.blanket.hs2205',
    'julun.switch.jlsw01',
    'kejia.airer.mznpro',
    'leishi.light.eps112',
    'leishi.light.eps118',
    'leshi.light.wyfan',
    'leshow.heater.bs1s',
    'leshow.heater.bs3',
    'leshow.heater.nfj1lx',
    'leshow.humidifier.jsq1',
    'linp.doorbell.g04',
    'linp.switch.q31',
    'linp.switch.q32',
    'linp.switch.q33',
    'lumi.acpartner.mcn04',
    'lumi.airer.acn02',
    'lumi.curtain.hagl05',
    'lumi.curtain.hagl08',
    'lumi.curtain.hmcn01',
    'lumi.sensor_gas.mcn02',
    'miaomiaoce.airm.air01',
    'miaomiaoce.blanket.s02',
    'mibx2.fridge.v1',
    'mibx2.washer.v5',
    'midjd6.fridge.v1',
    'mijia.vacuum.v1',
    'mijia.vacuum.v2',
    'minij.washer.v20',
    'mmgg.pet_waterer.s1',
    'mrbond.airer.m2',
    'msj.f_washer.m1pro',
    'nbczwl.airer.airer',
    'nnleaf.light.strips',
    'noc196.light.mdyctd',
    'nwt.derh.312en',
    'nwt.derh.330ef',
    'opple.bhf_light.acmoto',
    'opple.light.tabcw',
    'ows.tow_w.mjj20a',
    'ows.tow_w.mjjs1',
    # 'philips.light.bulb',  # issues/254
    # 'philips.light.cbulb',  # miio2miot
    'philips.light.dlight',
    'philips.light.sread3',
    'philips.light.strip2',
    'pwzn.light.apple',
    'pwzn.plug.banana',
    'qmi.plug.psv1',
    'qshui.blanket.d1',
    'qushui.bed.003',
    'roidmi.vacuum.v60',
    'roidmi.vacuum.v66',
    'skyrc.feeder.fed',
    'suittc.airrtc.wk168',
    'syi.airer.sy1',
    'szdy.airfresh.n80',
    'uvfive.s_lamp.slmap2',
    'uvfive.steriliser.tiger',
    'viewx.light.101001',
    'viomi.aircondition.y1',
    'viomi.aircondition.y69',
    'viomi.airer.vcy102',
    'viomi.airp.v3',
    'viomi.bhf_light.v3',
    'viomi.bhf_light.v4',
    'viomi.dishwasher.v06',
    'viomi.dishwasher.v07',
    'viomi.dishwasher.v11',
    'viomi.fan.v6',
    'viomi.fan.v7',
    'viomi.heater.v4',
    'viomi.heater.v6',
    'viomi.heater.vxtj01',
    'viomi.hood.c5',
    'viomi.hood.v2',
    'viomi.oven.so3',
    'viomi.vacuum.v12',
    'viomi.vacuum.v13',
    'viomi.vacuum.v15',
    'viomi.vacuum.v17',
    'viomi.vacuum.v18',
    'viomi.vacuum.v19',
    'viomi.vacuum.v23',
    'viomi.washer.v13',
    'viomi.washer.v19',
    'viomi.washer.v35',
    'viomi.washer.w1',
    'viomi.waterheater.e14',
    'viomi.waterheater.u22',
    'viomi.waterheater.u24',
    'viomi.waterheater.u27',
    'viomi.waterheater.u34',
    'viomi.waterheater.u42',
    'viomi.waterheater.u43',
    'xiaomi.aircondition.c12',
    'xiaomi.aircondition.c13',
    'xiaomi.aircondition.c15',
    'xiaomi.aircondition.c16',
    'xiaomi.aircondition.c19',
    'xiaomi.aircondition.mc4',
    'xiaomi.aircondition.mc5',
    'xiaomi.aircondition.mc7',
    'xiaomi.aircondition.mc8',
    'xiaomi.aircondition.mh1',
    'xiaomi.aircondition.mh2',
    'xiaomi.aircondition.mh4',
    'xiaomi.aircondition.mt1',
    'xiaomi.aircondition.mt2',
    'xiaomi.aircondition.mt3',
    'xiaomi.aircondition.mt4',
    'xiaomi.aircondition.mt6',
    'xiaomi.aircondition.mt7',
    'xiaomi.aircondition.mt8',
    'xiaomi.tv.4kh1',
    'xiaomi.tv.8kh1',
    'xiaomi.tv.dso1h1',
    'xiaomi.tv.eaffh1',
    'xiaomi.tv.eanfv1',
    'xiaomi.tv.esh1',
    'xiaomi.tv.fsi1',
    'xiaomi.tv.fsprov1',
    'xiaomi.tv.fsv1',
    'xiaomi.tv.mitv5h1',
    'xiaomi.tv.mitv5proh1',
    'xiaomi.tv.oledh1',
    'xiaomi.tv.rmaxv1',
    'xiaomi.tv.rmh1',
    'xiaomi.tv.rmi1',
    'xiaomi.tv.tv6h1',
    'xiaomi.tv.z2oh1',
    'xiaomi.tvbox.4prob1',
    'xinyue.blanket.n1918',
    'yeelink.bhf_light.v6',
    'yeelink.curtain.ctmt1',
    'yeelink.light.ceil26',
    'yeelink.light.ceil29',
    'yeelink.light.ceil34',
    'yeelink.light.ceila',
    'yeelink.light.ceilb',
    'yeelink.light.ceilc',
    # 'yeelink.light.color5',  # -9999
    'yeelink.light.colorb',
    'yeelink.light.colorc',
    'yeelink.light.fancl1',
    'yeelink.light.fancl2',
    'yeelink.light.fancl5',
    'yeelink.light.lamp15',
    'yeelink.light.lamp22',
    # 'yeelink.light.lamp4',  # miio2miot
    'yeelink.light.mono6',
    'yeelink.light.monoa',
    'yeelink.light.monob',
    'yeelink.light.stripa',
    'yeelink.switch.sw1',
    'yh1209.airer.public',
    'ymt.flowerpot.v1',
    'yuemee.sensor_gas.56712',
    'yunmi.waterpuri.f7',
    'yunmi.waterpuri.lx14',
    'yunmi.waterpuri.lx20',
    'yunmi.waterpuri.mg5',
    'yunmi.waterpuri.s10',
    'yunmi.waterpuri.s12',
    'yunmi.waterpuri.x10',
    'zdeer.foot_bath.zdz9',
    'zhimi.airfresh.ua1',
    'zhimi.airp.mb3a',
    'zhimi.airp.mb4a',
    'zhimi.airp.mb5',
    'zhimi.airp.mp4',
    'zhimi.airp.rmb1',
    'zhimi.airp.va2',
    'zhimi.airpurifier.ma4',
    'zhimi.airpurifier.mb3',
    'zhimi.airpurifier.mb4',
    'zhimi.airpurifier.rma1',
    'zhimi.airpurifier.va1',
    'zhimi.airpurifier.vb2',
    'zhimi.airpurifier.xa1',
    'zhimi.airpurifier.za1',
    'zhimi.fan.fa1',
    'zhimi.fan.fb1',
    'zhimi.fan.za5',
    'zhimi.heater.ma2a',
    'zhimi.heater.ma3',
    'zhimi.heater.ma4',
    'zhimi.heater.mc2',
    'zhimi.heater.na1',
    'zhimi.heater.nb1',
    'zhimi.heater.za2',
    'zhimi.heater.zb1',
    'zhimi.humidifier.ca4',
    'zhimi.humidifier.va1',
    'zhimi.vacuum.xa1',
]
