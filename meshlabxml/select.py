"""MeshLabXML selection functions"""


def deselect(script='TEMP3D_default.mlx', face=True,
             vert=True, current_layer=None, last_layer=None):
    """Clear the current set of selected faces

    Args:
        script (str): filename of the mlx script file to write to.
        faces (bool): If true the filter will deselect all the faces.
        verts (bool): If true the filter will deselect all the vertices.
        current_layer (int): number of the current layer
        last_layer (int): number of the last (highest numbered) layer

    Returns:
        current_layer, last_layer

    """
    script_file = open(script, 'a')
    script_file.write('  <filter name="Select None">\n')
    script_file.write(' '.join(['    <Param',
                               'name="allFaces"',
                               'value="%s"' % str(face).lower(),
                               'description="De-select all Faces"',
                               'type="RichBool"',
                               'tooltip="If true the filter will de-select all the faces."',
                               '/>\n']))
    script_file.write(' '.join(['    <Param',
                               'name="allVerts"',
                               'value="%s"' % str(vert).lower(),
                               'description="De-select all Vertices"',
                               'type="RichBool"',
                               'tooltip="If true the filter will de-select all the vertices."',
                               '/>\n']))
    script_file.write('  </filter>\n')
    """script_file.write('  <filter name="Select None">\n' +

             '    <Param name="allFaces" ' +
             'value="%s" ' % str(all_F).lower() +
             'description="De-select all Faces" ' +
             'type="RichBool" ' +
             'tooltip="If true the filter will de-select all the' +
             ' faces."/>\n' +

             '    <Param name="allVerts" ' +
             'value="%s" ' % str(all_V).lower() +
             'description="De-select all Vertices" ' +
             'type="RichBool" ' +
             'tooltip="If true the filter will de-select all the' +
             ' vertices."/>\n' +

             '  </filter>\n')"""
    script_file.close()
    return current_layer, last_layer


def invert(script='TEMP3D_default.mlx', face=True,
           vert=True, current_layer=None, last_layer=None):
    script_file = open(script, 'a')
    script_file.write('  <filter name="Invert Selection">\n' +

                      '    <Param name="InvFaces" ' +
                      'value="%s" ' % str(face).lower() +
                      'description="Invert Faces" ' +
                      'type="RichBool" ' +
                      'tooltip="If true  the filter will invert the selected' +
                      ' faces."/>\n' +

                      '    <Param name="InvVerts" ' +
                      'value="%s" ' % str(vert).lower() +
                      'description="Invert Vertices" ' +
                      'type="RichBool" ' +
                      'tooltip="If true the filter will invert the selected' +
                      ' vertices."/>\n' +

                      '  </filter>\n')
    script_file.close()
    return current_layer, last_layer


def border(script='TEMP3D_default.mlx',
           current_layer=None, last_layer=None):
    script_file = open(script, 'a')
    script_file.write('  <filter name="Select Border"/>\n')
    script_file.close()
    return current_layer, last_layer


def grow(script='TEMP3D_default.mlx', iterations=1,
         current_layer=None, last_layer=None):
    script_file = open(script, 'a')
    i = 0
    while i < iterations:
        script_file.write('  <filter name="Dilate Selection"/>\n')
        i += 1
    script_file.close()
    return current_layer, last_layer


def shrink(script='TEMP3D_default.mlx', iterations=1,
           current_layer=None, last_layer=None):
    script_file = open(script, 'a')
    i = 0
    while i < iterations:
        script_file.write('  <filter name="Erode Selection"/>\n')
        i += 1
    script_file.close()
    return current_layer, last_layer


def self_intersecting_face(script='TEMP3D_default.mlx',
                           current_layer=None, last_layer=None):
    script_file = open(script, 'a')
    script_file.write('  <filter name="Select Self Intersecting Faces"/>\n')
    script_file.close()
    return current_layer, last_layer


def nonmanifold_vert(script='TEMP3D_default.mlx',
                     current_layer=None, last_layer=None):
    script_file = open(script, 'a')
    script_file.write('  <filter name="Select non Manifold Vertices"/>\n')
    script_file.close()
    return current_layer, last_layer


def nonmanifold_edge(script='TEMP3D_default.mlx',
                     current_layer=None, last_layer=None):
    script_file = open(script, 'a')
    script_file.write('  <filter name="Select non Manifold Edges"/>\n')
    script_file.close()
    return current_layer, last_layer


def small_parts(script='TEMP3D_default.mlx', ratio=0.2,
                non_closed_only=False, current_layer=None, last_layer=None):
    script_file = open(script, 'a')
    script_file.write('  <filter name="Small component selection">\n' +

                      '    <Param name="NbFaceRatio" ' +
                      'value="%s" ' % ratio +
                      'description="Small component ratio" ' +
                      'type="RichFloat" ' +
                      'tooltip="This ratio (between 0 and 1) defines the meaning of' +
                      ' _small_as the threshold ratio between the number of faces of' +
                      ' the largest component and the other ones. A larger value' +
                      ' will select more components."/>\n' +

                      '    <Param name="NonClosedOnly" ' +
                      'value="%s" ' % str(non_closed_only).lower() +
                      'description="Select only non closed components" ' +
                      'type="RichBool" ' +
                      'tooltip="Select only non-closed components."/>\n' +

                      '  </filter>\n')
    script_file.close()
    return current_layer, last_layer


def vert_quality(script='TEMP3D_default.mlx', min_quality=0.0, max_quality=0.05,
                 inclusive=True, current_layer=None, last_layer=None):
    # TODO: set min & max better
    script_file = open(script, 'a')
    script_file.write('  <filter name="Select by Vertex Quality">\n' +

                      '    <Param name="minQ" ' +
                      'value="%s" ' % min_quality +
                      'description="Min Quality" ' +
                      'min="0" ' +
                      'max="0.1" ' +
                      'type="RichDynamicFloat" ' +
                      'tooltip="Minimum acceptable quality value."/>\n' +

                      '    <Param name="maxQ" ' +
                      'value="%s" ' % max_quality +
                      'description="Max Quality" ' +
                      'min="0" ' +
                      'max="0.1" ' +
                      'type="RichDynamicFloat" ' +
                      'tooltip="Maximum acceptable quality value."/>\n' +

                      '    <Param name="Inclusive" ' +
                      'value="%s" ' % str(inclusive).lower() +
                      'description="Inclusive Sel." ' +
                      'type="RichBool" ' +
                      'tooltip="If true only the faces with _all_ the vertices' +
                      ' within the specified range are selected. Otherwise any face' +
                      ' with at least one vertex within the range is selected."/>\n' +

                      '  </filter>\n')
    script_file.close()
    return current_layer, last_layer


def face_function(script='TEMP3D_default.mlx',
                  function='(fi == 0)', current_layer=None, last_layer=None):
    script_file = open(script, 'a')
    script_file.write('  <filter name="Conditional Face Selection">\n'

                      + '    <Param name="condSelect" '
                      + 'value="%s" ' % function.replace('<', '&lt;')
                      + 'description="boolean function" '
                      + 'type="RichString" '
                      + 'tooltip="type a boolean function that will be evaluated in order to select a subset of faces"/>\n'

                      + '  </filter>\n')
    script_file.close()
    return current_layer, last_layer


def vert_function(script='TEMP3D_default.mlx', function='(q < 0)',
                  strict_face_select=True, current_layer=None, last_layer=None):
    script_file = open(script, 'a')
    script_file.write('  <filter name="Conditional Vertex Selection">\n'

                      + '    <Param name="condSelect" '
                      + 'value="%s" ' % function.replace('<', '&lt;')
                      + 'description="boolean function" '
                      + 'type="RichString" '
                      + 'tooltip="type a boolean function that will be evaluated in order to select a subset of vertices. Example: (y > 0) and (ny > 0)"/>\n'

                      + '    <Param name="strictSelect" '
                      + 'value="%s" ' % str(strict_face_select).lower()
                      + 'description="Strict face selection" '
                      + 'type="RichBool" '
                      + 'tooltip="If checked a face is selected if ALL its vertices are selected. If unchecked a face is selected if at least one of its vertices is selected."/>\n'

                      + '  </filter>\n')
    script_file.close()
    return current_layer, last_layer
