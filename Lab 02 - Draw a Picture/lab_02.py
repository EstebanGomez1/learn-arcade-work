"""
SESION DE LABORATORIO 2: DIBUJO DE COCHE SUPERDEPORTIVO

ESTEBAN GOMEZ.
"""

import arcade
arcade.open_window(800, 600, "Drawing Example")
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()

#dibujamos el asfalto
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.GRAY)

#REJILLA DE PARABRISAS TRASERO
arcade.draw_rectangle_filled(370, 366, 20, 10, arcade.color.BLACK)
arcade.draw_rectangle_filled(336, 356, 20, 10, arcade.color.BLACK)
arcade.draw_rectangle_filled(300, 346, 20, 10, arcade.color.BLACK)
arcade.draw_rectangle_filled(268, 336, 20, 10, arcade.color.BLACK)

#ALERON
arcade.draw_rectangle_filled(180, 300, 10, 50, arcade.color.BLACK)
arcade.draw_rectangle_filled(160, 300, 10, 55, arcade.color.BLACK)
arcade.draw_triangle_filled(130, 330, 200, 320, 130, 345, arcade.color.BLACK)


#CARROCERIA
arcade.draw_rectangle_filled(425, 260, 575, 70, arcade.color.RED)
arcade.draw_triangle_filled(710, 295, 250, 260, 430, 350, arcade.color.RED)
arcade.draw_triangle_filled(710, 230, 150, 230, 430, 385, arcade.color.RED)
arcade.draw_triangle_filled(130, 295, 150, 230, 430, 385, arcade.color.RED)

#VENTANA Y PICAPORTE
arcade.draw_triangle_filled(525, 310, 250, 310, 420, 365, arcade.color.WHITE)
arcade.draw_rectangle_filled(375, 300, 14, 125, arcade.color.RED)
arcade.draw_rectangle_filled(400, 290, 14, 10, arcade.color.BLACK)


#DIBUJAMOS LAS RUEDAS DELANTE
arcade.draw_circle_filled(600, 250, 50, arcade.color.BLACK)
arcade.draw_circle_filled(600, 250, 45, arcade.color.BLACK_OLIVE)
arcade.draw_circle_filled(600, 225, 20, arcade.color.BLACK)
arcade.draw_circle_filled(600, 275, 20, arcade.color.BLACK)
arcade.draw_circle_filled(575, 250, 20, arcade.color.BLACK)
arcade.draw_circle_filled(625, 250, 20, arcade.color.BLACK)
arcade.draw_circle_filled(600, 250, 10, arcade.color.RED)

#DIBUJAMOS LAS RUEDAS ATRAS
arcade.draw_circle_filled(200, 250, 50, arcade.color.BLACK)
arcade.draw_circle_filled(200, 250, 45, arcade.color.BLACK_OLIVE)
arcade.draw_circle_filled(200, 225, 20, arcade.color.BLACK)
arcade.draw_circle_filled(200, 275, 20, arcade.color.BLACK)
arcade.draw_circle_filled(175, 250, 20, arcade.color.BLACK)
arcade.draw_circle_filled(225, 250, 20, arcade.color.BLACK)
arcade.draw_circle_filled(200, 250, 10, arcade.color.RED)



arcade.finish_render()
arcade.run()