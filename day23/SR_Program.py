

def createRefballShader():
    matnode = hou.node('/mat/').createNode('arnold_materialbuilder', 'REFBALL')
    matnode.moveToGoodPosition()

    matspyderChecker = matnode.createNode('arnold_material', 'spyderChecker_mat')
    matspyderChecker_shader = matnode.createNode('arnold::standard_surface')
    matspyderChecker_tex = matnode.createNode('arnold::image', 'matspyderChecker_tex')
    matspyderChecker_tex.parm('filename').set(
        '/show/Assets/assets/lit/referenceBall/lookdev/wip/sourceimages/tx/arnold/MacbethTarget_datacolor_Lab_new_srgb.tx')
    matspyderChecker_tex.parm('/mat/REFBALL/matspyderChecker_tex/swap_st').set('1')
    matspyderChecker_tex.parm('/mat/REFBALL/matspyderChecker_tex/tflip').set('1')

    matspyderChecker_shader.parm('base').set('1')
    matspyderChecker_shader.parm('specular_roughness').set('0.99')

    matspyderChecker.setInput(0, matspyderChecker_shader)
    matspyderChecker_shader.setInput(1, matspyderChecker_tex)
    matspyderChecker_shader.setInput(5, matspyderChecker_tex)

    matgreyball = matnode.createNode('arnold_material', 'matgreyball_mat')
    matgreyball_mix_shader = matnode.createNode('arnold::mix_shader')
    matgreyball_ramp = matnode.createNode('arnold::ramp_rgb')
    matgreyball_shader1 = matnode.createNode('arnold::standard_surface')
    matgreyball_shader2 = matnode.createNode('arnold::standard_surface')
    matgreyball_tex = matnode.createNode('arnold::image')
    matgreyball_tex.parm('filename').set(
        '/show/Assets/assets/lit/referenceBall/lookdev/wip/sourceimages/tx/arnold/black_squares_50grey.tx')

    matgreyball_shader1.parm('base').set('1')
    matgreyball_shader1.parm('specular_roughness').set('0.53')
    matgreyball_shader1.parm('specular').set('0.1')
    matgreyball_shader1.parm('specular_colorr').set('0.332')
    matgreyball_shader1.parm('specular_colorg').set('0.332')
    matgreyball_shader1.parm('specular_colorb').set('0.332')

    matgreyball_shader2.parm('base').set('1')
    matgreyball_shader2.parm('specular_roughness').set('0.4')
    matgreyball_shader2.parm('specular').set('0.1')
    matgreyball_shader2.parm('specular_colorr').set('0.571')
    matgreyball_shader2.parm('specular_colorg').set('0.571')
    matgreyball_shader2.parm('specular_colorb').set('0.571')

    matgreyball_ramp.parm('ramp').set(3)
    matgreyball_ramp.parm('ramp2pos').set('0.62')
    matgreyball_ramp.parm('ramp3pos').set('0.853')

    matgreyball_ramp.parm('ramp1cr').set('0.48')
    matgreyball_ramp.parm('ramp1cg').set('0.48')
    matgreyball_ramp.parm('ramp1cb').set('0.48')

    matgreyball_ramp.parm('ramp2cr').set('0.097')
    matgreyball_ramp.parm('ramp2cg').set('0.097')
    matgreyball_ramp.parm('ramp2cb').set('0.097')

    matgreyball_ramp.parm('ramp3cr').set('0')
    matgreyball_ramp.parm('ramp3cg').set('0')
    matgreyball_ramp.parm('ramp3cb').set('0')

    matgreyball.setInput(0, matgreyball_mix_shader)
    matgreyball_mix_shader.setInput(1, matgreyball_ramp)
    matgreyball_mix_shader.setInput(2, matgreyball_shader1)
    matgreyball_mix_shader.setInput(3, matgreyball_shader2)
    matgreyball_shader1.setInput(1, matgreyball_tex)
    matgreyball_shader2.setInput(1, matgreyball_tex)

    matchrome = matnode.createNode('arnold_material', 'matchrome')
    matchrome_shader = matnode.createNode('arnold::standard_surface')

    matchrome_shader.parm('base').set('1')
    matchrome_shader.parm('metalness').set('1')
    matchrome_shader.parm('specular_roughness').set('0')

    matchrome.setInput(0, matchrome_shader)

    matbeachBall = matnode.createNode('arnold_material', 'matbeachBall')
    matbeachBall_shader = matnode.createNode('arnold::standard_surface')
    matbeachBall_tex = matnode.createNode('arnold::image')
    matbeachBall_tex.parm('filename').set(
        '/show/Assets/assets/lit/referenceBall/lit/wip/sourceimages/tx/arnold/beachBall_v02.1001.tx')

    matbeachBall_shader.parm('base').set('1')
    matbeachBall_shader.parm('specular_colorr').set('0.571')
    matbeachBall_shader.parm('specular_colorg').set('0.571')
    matbeachBall_shader.parm('specular_colorb').set('0.571')
    matbeachBall_shader.parm('specular_roughness').set('0.025')

    matbeachBall.setInput(0, matbeachBall_shader)
    matbeachBall_shader.setInput(1, matbeachBall_tex)

    matcardblack = matnode.createNode('arnold_material', 'matcardblack')
    matcardblack_shader = matnode.createNode('arnold::standard_surface')
    matcardblack_tex = matnode.createNode('arnold::image')
    matcardblack_tex.parm('filename').set(
        '/show/Assets/assets/lit/referenceBall/lookdev/wip/sourceimages/tiff/arnold/steelBe_rec709/black_squares_black_rec709.tx')

    matcardblack_shader.parm('base').set('1')
    matcardblack_shader.parm('specular').set('0')
    matcardblack_shader.parm('specular_colorr').set('0.571')
    matcardblack_shader.parm('specular_colorg').set('0.571')
    matcardblack_shader.parm('specular_colorb').set('0.571')

    matcardblack.setInput(0, matcardblack_shader)
    matcardblack_shader.setInput(1, matcardblack_tex)

    matspecball = matnode.createNode('arnold_material', 'matspecball')
    matspecball_shader = matnode.createNode('arnold::standard_surface')

    matspecball_shader.parm('base').set('0')
    matspecball_shader.parm('specular').set('1')
    matspecball_shader.parm('metalness').set('1')
    matspecball_shader.parm('specular_colorr').set('0.571')
    matspecball_shader.parm('specular_colorg').set('0.571')
    matspecball_shader.parm('specular_colorb').set('0.571')
    matspecball_shader.parm('specular_roughness').set('0.15')

    matspecball.setInput(0, matspecball_shader)

    matfigure = matnode.createNode('arnold_material', 'matfigure')
    matfigure_shader = matnode.createNode('arnold::standard_surface')

    matfigure_shader.parm('base').set('1')
    matfigure_shader.parm('base_colorr').set('0.567')
    matfigure_shader.parm('base_colorg').set('0.564201')
    matfigure_shader.parm('base_colorb').set('0.562464')
    matfigure_shader.parm('specular').set('1')
    matfigure_shader.parm('specular_colorr').set('0.571')
    matfigure_shader.parm('specular_colorg').set('0.571')
    matfigure_shader.parm('specular_colorb').set('0.571')

    matfigure.setInput(0, matfigure_shader)

    mattumbler_bottle = matnode.createNode('arnold_material', 'mattumbler_bottle')
    mattumbler_bottle_shader = matnode.createNode('arnold::standard_surface')

#리팩토링

    mattumbler_bottle_shader.parm('base').set('1')
    mattumbler_bottle_shader.parm('base_colorr').set('0.38')
    mattumbler_bottle_shader.parm('base_colorg').set('0.38')
    mattumbler_bottle_shader.parm('base_colorb').set('0.38')
    mattumbler_bottle_shader.parm('metalness').set('0.8')
    mattumbler_bottle_shader.parm('specular_colorr').set('0.552')
    mattumbler_bottle_shader.parm('specular_colorg').set('0.552')
    mattumbler_bottle_shader.parm('specular_colorb').set('0.552')
    mattumbler_bottle_shader.parm('specular_roughness').set('0.11')
    mattumbler_bottle_shader.parm('specular_IOR').set('16')
    mattumbler_bottle_shader.parm('coat').set('0.35')
    mattumbler_bottle_shader.parm('coat_colorr').set('0.571')
    mattumbler_bottle_shader.parm('coat_colorg').set('0.571')
    mattumbler_bottle_shader.parm('coat_colorb').set('0.571')
    mattumbler_bottle_shader.parm('coat_roughness').set('0.5')
    mattumbler_bottle_shader.parm('coat_IOR').set('16')

    mattumbler_bottle.setInput(0, mattumbler_bottle_shader)

    mattumbler_lid = matnode.createNode('arnold_material', 'mattumbler_lid')
    mattumbler_lid_shader = matnode.createNode('arnold::standard_surface')

    mattumbler_lid_shader.parm('base').set('1')
    mattumbler_lid_shader.parm('base_colorr').set('0.372')
    mattumbler_lid_shader.parm('base_colorg').set('0.372')
    mattumbler_lid_shader.parm('base_colorb').set('0.372')
    mattumbler_lid_shader.parm('specular').set('0.2')
    mattumbler_lid_shader.parm('specular_colorr').set('0.481')
    mattumbler_lid_shader.parm('specular_colorg').set('0.481')
    mattumbler_lid_shader.parm('specular_colorb').set('0.481')
    mattumbler_lid_shader.parm('specular_roughness').set('0.5')
    mattumbler_lid_shader.parm('specular_IOR').set('0')
    matglassbottle_glass_shader.parm('transmission_scatterg').set('0.093')
    matglassbottle_glass_shader.parm('transmission_scatterb').set('0.093')

    matglassbottle_glass.setInput(0, matglassbottle_glass_shader)

    matglassbottle_lid = matnode.createNode('arnold_material', 'matglassbottle_lid')
    matglassbottle_lid_shader = matnode.createNode('arnold::standard_surface')

    matglassbottle_lid_shader.parm('base_colorr').set('0.569')
    matglassbottle_lid_shader.parm('base_colorg').set('0.546531')
    matglassbottle_lid_shader.parm('base_colorb').set('0.50641')
    matglassbottle_lid_shader.parm('metalness').set('0.65')
    matglassbottle_lid_shader.parm('specular').set('0.65')
    matglassbottle_lid_shader.parm('specular_colorr').set('0.569')
    matglassbottle_lid_shader.parm('specular_colorg').set('0.554305')
    matglassbottle_lid_shader.parm('specular_colorb').set('0.524049')
    matglassbottle_lid_shader.parm('specular_roughness').set('0.25')

    mattumbler_lid.setInput(0, mattumbler_lid_shader)

    matglassbottle_glass = matnode.createNode('arnold_material', 'matglassbottle_glass')
    matglassbottle_glass_shader = matnode.createNode('arnold::standard_surface')

    matglassbottle_glass_shader.parm('metalness').set('0')
    matglassbottle_glass_shader.parm('specular').set('0.1')
    matglassbottle_glass_shader.parm('specular_colorr').set('0.571')
    matglassbottle_glass_shader.parm('specular_colorg').set('0.571')
    matglassbottle_glass_shader.parm('specular_colorb').set('0.571')
    matglassbottle_glass_shader.parm('specular_IOR').set('2')
    matglassbottle_glass_shader.parm('transmission').set('1')
    matglassbottle_glass_shader.parm('transmission_colorr').set('0.571')
    matglassbottle_glass_shader.parm('transmission_colorg').set('0.571')
    matglassbottle_glass_shader.parm('transmission_colorb').set('0.571')
    matglassbottle_glass_shader.parm('transmission_scatterr').set('0.093')

    matglassbottle_lid.setInput(0, matglassbottle_lid_shader)

    matbump2d = matnode.createNode('arnold::bump2d')
    matbump2d_noise = matnode.createNode('arnold::cell_noise')


    matbump2d_noise.parm('pattern').set('2')
    matbump2d_noise.parm('octaves').set('6')
    matbump2d_noise.parm('lacunarity').set('4.4')
    matbump2d_noise.parm('randomness').set('0.034')
    matbump2d_noise.parm('amplitude').set('6.08')
    matbump2d_noise.parm('scalex').set('10')
    matbump2d_noise.parm('scaley').set('10')
    matbump2d_noise.parm('scalez').set('10')
    matbump2d_noise.parm('colorr').set('0.497')
    matbump2d_noise.parm('colorg').set('0.497')
    matbump2d_noise.parm('colorb').set('0.497')
    matbump2d_noise.parm('density').set('0')
    matbump2d_noise.parm('time').set('0.235')

    matbump2d.setInput(0, matbump2d_noise)

    matcan = matnode.createNode('arnold_material', 'matcan')
    matcan_shader = matnode.createNode('arnold::standard_surface')

    matcan_shader.parm('base').set('1')
    matcan_shader.parm('base_colorr').set('0.871')
    matcan_shader.parm('base_colorg').set('0.871')
    matcan_shader.parm('base_colorb').set('0.871')
    matcan_shader.parm('metalness').set('1')
    matcan_shader.parm('specular').set('0.52')
    matcan_shader.parm('specular_colorr').set('0.553')
    matcan_shader.parm('specular_colorg').set('0.553')
    matcan_shader.parm('specular_colorb').set('0.553')
    matcan_shader.parm('specular_roughness').set('0.27')

    matcan.setInput(0, matcan_shader)

    matnode.layoutChildren()


createRefballShader()


def createRefball():
    alembic_list = []

    subnetnode = hou.node('/obj/').createNode('subnet', 'REFBALL')
    subnetnode.moveToGoodPosition()

    spyderChecker = subnetnode.createNode('geo', 'spyderChecker')
    spyderCheckerabc = spyderChecker.createNode('alembic', 'spyderCheckerabc')
    spyderCheckerabc.parm('fileName').set(Config.COMMON_FILE_PATH + spyderChecker.abc')

    spyderChecker.parm('shop_materialpath').set('/mat/REFBALL/spyderChecker_mat')

    alembic_list.append(spyderCheckerabc)

    beachBall = subnetnode.createNode('geo', 'beachBall')
    beachBallabc = beachBall.createNode('alembic', 'beachBallabc')
    beachBallabc.parm('fileName').set('/show/KINGDOM/assets/LIT/ref_ball/alembic/beachBall.abc')

    beachBall.parm('shop_materialpath').set('/mat/REFBALL/matbeachBall')

    alembic_list.append(beachBallabc)

    chromeBall = subnetnode.createNode('geo', 'chromeBall')
    chromeBallabc = chromeBall.createNode('alembic', 'chromeBallabc')
    chromeBallabc.parm('fileName').set('/show/KINGDOM/assets/LIT/ref_ball/alembic/chromeBall.abc')
    chromeBall.parm('shop_materialpath').set('/mat/REFBALL/matchrome')

    alembic_list.append(chromeBallabc)

    cardBlackBall = subnetnode.createNode('geo', 'cardBlackBall')
    cardBlackBallabc = cardBlackBall.createNode('alembic', 'cardBlackBallabc')
    cardBlackBallabc.parm('fileName').set('/show/KINGDOM/assets/LIT/ref_ball/alembic/cardBlackBall.abc')
    cardBlackBall.parm('shop_materialpath').set('/mat/REFBALL/matcardblack')

    alembic_list.append(cardBlackBallabc)

    specball = subnetnode.createNode('geo', 'specball')
    specballabc = specball.createNode(Config.NODE_TYPE, 'specballabc')
    specballabc.parm('fileName').set('/show/KINGDOM/assets/LIT/ref_ball/alembic/specBall.abc')
    specball.parm('shop_materialpath').set('/mat/REFBALL/matspecball')
    alembic_list.append(specballabc)

    greyBall = subnetnode.createNode('geo', 'greyBall')
    greyBallabc = greyBall.createNode('alembic', 'greyBallabc')
    greyBallabc.parm('fileName').set('/show/KINGDOM/assets/LIT/ref_ball/alembic/greyBall.abc')
    greyBall.parm('shop_materialpath').set('/mat/REFBALL/matgreyball_mat')

    alembic_list.append(greyBallabc)

    figure = subnetnode.createNode('geo', 'figure')
    figureabc = figure.createNode('alembic', 'figureabc')
    figureabc.parm('fileName').set('/show/KINGDOM/assets/LIT/ref_ball/alembic/figure.abc')
    figure.parm('shop_materialpath').set('/mat/REFBALL/matfigure')

    alembic_list.append(figureabc)

    tumbler_bottle = subnetnode.createNode('geo', 'tumbler_bottle')
    tumbler_bottleabc = tumbler_bottle.createNode('alembic', 'tumbler_bottleabc')
    tumbler_bottleabc.parm('fileName').set('/show/KINGDOM/assets/LIT/ref_ball/alembic/tumbler.abc')
    tumbler_bottle.parm('shop_materialpath').set('/mat/REFBALL/mattumbler_bottle')

    create_blast1 = tumbler_bottle.createNode('blast', 'tumbler_bottle_blast')
    create_blast1.setInput(0, tumbler_bottleabc)
    create_blast1.parm('group').set('1')
    create_blast1.setDisplayFlag(True)
    create_blast1.setRenderFlag(True)
    alembic_list.append(create_blast1)

    tumbler_lid = subnetnode.createNode('geo', 'tumbler_lid')
    tumbler_lidabc = tumbler_lid.createNode('alembic', 'tumbler_lidabc')
    tumbler_lidabc.parm('fileName').set('/show/KINGDOM/assets/LIT/ref_ball/alembic/tumbler.abc')
    tumbler_lid.parm('shop_materialpath').set('/mat/REFBALL/mattumbler_lid')

    create_blast2 = tumbler_lid.createNode('blast', 'tumbler_lid_blast')
    create_blast2.setInput(0, tumbler_lidabc)
    create_blast2.parm('group').set('0')
    create_blast2.setDisplayFlag(True)
    create_blast2.setRenderFlag(True)
    alembic_list.append(create_blast2)

    glassBottle_glass = subnetnode.createNode('geo', 'glassBottle_glass')
    glassBottle_glassabc = glassBottle_glass.createNode('alembic', 'glassBottle_glassabc')
    glassBottle_glassabc.parm('fileName').set('/show/KINGDOM/assets/LIT/ref_ball/alembic/glassBottle.abc')
    glassBottle_glass.parm('shop_materialpath').set('/mat/REFBALL/matglassbottle_glass')

    create_blast3 = glassBottle_glass.createNode('blast', 'glassBottle_glass_blast')
    create_blast3.setInput(0, glassBottle_glassabc)
    create_blast3.parm('group').set('0')
    create_blast3.setDisplayFlag(True)
    create_blast3.setRenderFlag(True)
    alembic_list.append(create_blast3)

    glassBottle_lid = subnetnode.createNode('geo', 'glassBottle_lid')
    glassBottle_lidabc = glassBottle_lid.createNode('alembic', 'glassBottle_lidabc')
    glassBottle_lidabc.parm('fileName').set('/show/KINGDOM/assets/LIT/ref_ball/alembic/glassBottle.abc')
    glassBottle_lid.parm('shop_materialpath').set('/mat/REFBALL/matglassbottle_lid')

    create_blast4 = glassBottle_glass.createNode('blast', 'glassBottle_lid_blast')
    create_blast4.setInput(0, glassBottle_glassabc)
    create_blast4.parm('group').set('0')
    create_blast4.setDisplayFlag(True)
    create_blast4.setRenderFlag(True)
    alembic_list.append(create_blast4)

    can = subnetnode.createNode('geo', 'can')
    canabc = can.createNode('alembic', 'canabc')
    canabc.parm('fileName').set('/show/KINGDOM/assets/LIT/ref_ball/alembic/can.abc')
    can.parm('shop_materialpath').set('/mat/REFBALL/matcan')

    alembic_list.append(canabc)

    subnetnode.layoutChildren()


createRefball()

builder = hou.node('/mat/').createNode('arnold_materialbuilder','projection')
material = builder.createNode('arnold_material')
shadow_matte = builder.createNode('arnold::shadow_matte', 'projection_matte')
cam = builder.createNode('arnold::camera_projection')
image = builder.createNode('arnold::image')

material.setInput(0,shadow_matte)
shadow_matte.setInput(1,cam)
cam.setInput(0,image)
cam.setInput(1,image)

shadow_matte.parm('background').set('1')

builder.layoutChildren()
