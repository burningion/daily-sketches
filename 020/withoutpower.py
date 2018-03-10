import pyglet

from pyglet import gl

window = pyglet.window.Window(1920, 1080, fullscreen=True)
window.set_mouse_visible(False)
window.config.alpha_size = 8

main_batch = pyglet.graphics.Batch()
#sprite = pyglet.resource.image('fpl_logo.png')

x1, y1 = 0, 0

pyglet.gl.glClearColor(1,1,1,1)

@window.event
def on_mouse_motion(x, y, dx, dy):
    global x1, y1
    x1, y1 = x, y

@window.event
def on_draw():
    window.clear()
    gl.glEnable(gl.GL_BLEND)

    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
    #sprite.blit(x1, y1)

    for i in range(10):
        labely = pyglet.text.Label(text="no power today", x=x1, y=y1 + 30 * i, batch=main_batch, color=(0,0,0,255))


    #sprite.batch = main_batch
    main_batch.draw()


pyglet.app.run()
