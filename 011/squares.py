# original setup and example vertex and fragment shader from the
# glumpy docs. see copyright below
# -----------------------------------------------------------------------------
# Copyright (c) 2009-2016 Nicolas P. Rougier. All rights reserved.
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
# I wouldn't use this code as an example really. This was mostly me
# figuring out how the hell shaders work, and is mostly the wrong approach.

from glumpy import app, gl, gloo
from glumpy.ext import png
import numpy as np

vertex = """
attribute vec2 position;
void main (void)
{
    gl_Position = vec4(1.0*position, 0.0, 1.0);
}
"""

fragment = """
uniform vec3 color;
uniform vec2 resolution;
uniform float time;

#define PI 3.14159265359

mat2 rotate2d(float _angle){
    return mat2(cos(_angle),-sin(_angle),
                sin(_angle),cos(_angle));
}

float box(in vec2 _st, in vec2 _size){
    _size = vec2(0.5) - _size*0.5;
    vec2 uv = smoothstep(_size,
                        _size+vec2(0.001),
                        _st);
    uv *= smoothstep(_size,
                    _size+vec2(0.001),
                    vec2(1.0)-_st);
    return uv.x*uv.y;
}

void main(void)
{
    vec2 st = gl_FragCoord.xy / resolution.xy;
    vec3 color1 = vec3(0.0);
    st -= vec2(0.5);
    st = rotate2d( sin(time) * PI) * st;
    st += vec2(0.5);
    color1 += vec3(box(st, vec2(0.8, 0.8)));
    //gl_FragColor = vec4(color1 * color, 0.9);
    gl_FragColor = vec4(color, 0.9);
}
"""

# noise part of shader below comes from
# @manoloide: https://twitter.com/manoloidee/status/955137757436895239

fragment1 = """
#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

uniform vec2 resolution;
uniform float time;

uniform vec3 colorA;
uniform vec3 colorB;

varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;

varying vec4 vertTexCoord;

#define PI 3.14159265359

mat2 rotate2d(float _angle){
    return mat2(cos(_angle),-sin(_angle),
                sin(_angle),cos(_angle));
}

float box(in vec2 _st, in vec2 _size){
    _size = vec2(0.5) - _size*0.5;
    vec2 uv = smoothstep(_size,
                        _size+vec2(0.001),
                        _st);
    uv *= smoothstep(_size,
                    _size+vec2(0.001),
                    vec2(1.0)-_st);
    return uv.x*uv.y;
}


float rand(vec2 co){
    return fract(sin(dot(co.xy, vec2(12.9898,78.233))) * 43758.5453);
}


void main(void)
{
    vec2 st = gl_FragCoord.xy/resolution;
    vec3 color = vec3(0.0);
    float pct = abs(sin(time));

    st -= vec2(0.5);
    st = rotate2d( sin(time) * PI * .5) * st;
    st += vec2(0.5);

    color = mix(colorA, colorB, pct);
    color = color * st.x;
    vec4 color1 = vec4(color, 0.8);

    vec4 color2 = vec4(0.0);
    color2 += vec4(vec3(box(st, vec2(5.0, 0.7))), 1.0);

    color1.a *= pow(rand(gl_FragCoord.xy*0.01), 0.8);
    gl_FragColor = color1 * color2;
}
"""

window = app.Window(width=1000, height=1000, fullscreen=True)

dt = 0.001

quads = []

counter = 1
framebuffer = np.zeros((window.height, window.width * 3), dtype=np.uint8)

@window.event
def on_draw(dt):
    global counter
    window.clear()
    for quadies in quads[::-1]:
        quadies[0].draw(gl.GL_TRIANGLE_STRIP)
        
        quadies[1].draw(gl.GL_TRIANGLE_STRIP)
        quadies[2].draw(gl.GL_TRIANGLE_STRIP)
        
        
        
        
        quadies[0]['time'] += dt
        quadies[1]['time'] += dt
        quadies[2]['time'] += dt
    #gl.glReadPixels(0, 0, window.width, window.height,
    #                gl.GL_RGB, gl.GL_UNSIGNED_BYTE, framebuffer)
    #png.from_array(framebuffer, 'RGB').save('imageseq/%05d.png' % counter)
    #counter += 1
    #if counter == 900:
    #    exit()
for j in range(6):
    i = float(j) / 5
    quad = gloo.Program(vertex, fragment, count=4)
    quad['position'] = [(-1 * i,-1 * i), (-1 * i,+1 * i), (+1 * i,-1 * i), (+1 * i,+1 * i)]
    if i <= 0.4:
        quad['color'] = [0.065, 0.066, 0.290]
    else:
        quad['color'] = [0.065 * i * 2, 0.066 * i * 2, 0.290 * i * 2]
    quad['resolution'] = [800 * i, 800 * i]
    quad1 = gloo.Program(vertex, fragment1, count=4)
    quad2 = gloo.Program(vertex, fragment1, count=4)
    quad1['colorA'] = [0.418 * j, 0.735 * j, 0.780 * j]
    quad1['colorB'] = [0.980 * j, 0.603 * j, 0.086 * j]
    quad2['colorA'] = [0.980, 0.603, 0.086]
    quad2['colorB'] = [0.418, 0.735, 0.780]
    quad2['position'] = [(-0.6 * i, -0.6 * i),
                         (-0.6 * i, +0.6 * i),
                         (+0.6 * i, -0.6 * i),
                         (+0.6 * i, +0.6 * i)]
    quad1['position'] = [(-1.2 * i, -1.2 * i),
                         (-1.2 * i, +1.2 * i),
                         (+1.2 * i, -1.2 * i),
                         (+1.2 * i, +1.2 * i)]
    quad1['resolution'] = [1200 * i, 1200 * i]
    quad2['resolution'] = [1200, 1200]
    quads.append([quad, quad1, quad2])

app.run()
