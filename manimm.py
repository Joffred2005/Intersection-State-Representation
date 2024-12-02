from manim import *
import numpy
import pandas as pd
import os

class VideoExample (MovingCameraScene):
    def construct(self):
        
    
        text = Text("Team 11 Demo").scale(1)
        self.play(
            Write(text),
            run_time=3
            )
        self.wait(1)
        self.play(Unwrite(text))
        
        text1 = Text("Traffic Congestion").scale(1)
        self.play(
            Write(text1),
            run_time=2
            )
        self.wait(1)
        self.play(Unwrite(text1))
        

        number_plane = NumberPlane(
            x_range=(1, 4, 1),
            y_range=(1, 4, 1),
            x_length=6,
            y_length=6,
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )

        number_plane.axes.set_opacity(0)

        intersectionsVal = {
            "x" : [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
            "y" : [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
        }
        
        dfinter = pd.DataFrame(intersectionsVal)
        
        # Calculate exact corner points for the border rectangle
        x_min, x_max = number_plane.x_range[0], number_plane.x_range[1]
        y_min, y_max = number_plane.y_range[0], number_plane.y_range[1]

        # Create a rectangle that aligns with the outermost grid lines
        grid_border = Polygon(
            number_plane.c2p(x_min, y_min),  # Bottom-left corner
            number_plane.c2p(x_max, y_min),  # Bottom-right corner
            number_plane.c2p(x_max, y_max),  # Top-right corner
            number_plane.c2p(x_min, y_max),  # Top-left corner
            color=TEAL,
            stroke_width=4
        )
        intersection = [Dot(number_plane.c2p  (x,y), color=BLUE) for x, y in dfinter.values]

        self.play(Write(grid_border))
        self.play(Write(number_plane))
        self.play(LaggedStart(*[Write(dot) for dot in intersection], lag_ratio=.05))
        
        self.wait(1)

        brace1 = Brace(number_plane, direction=LEFT)  # Add the brace to the left side
        brace2 = Brace(number_plane, direction=UP)

        brace1_lab=Text("4 Intesections").next_to(brace1, LEFT, buff=0.01)
        brace1_lab.shift(RIGHT*1.5)
        brace1_lab.rotate(3.14159265358979323846264338327950288419716939937510/2)
        brace2_lab=Text("4 Intesections").next_to(brace2, UP, buff=0.01)

        brace1_lab.scale(0.5)
        brace2_lab.scale(0.5)

        # Add the number plane, brace, and label to the scene
        self.play(
            Write(brace1),
            Write(brace2),
            Write(brace1_lab),
            Write(brace2_lab)
            )

        self.wait(3)

        # Define the point to zoom into (using a specific mobject)
        target_point = Dot(number_plane.c2p(3, 3), color=RED)  # Point (3, 3)

        # Add the target point
        self.add(target_point)

        # Animate camera movement and zoom
        self.play(
            self.camera.auto_zoom([target_point], margin=1.5),
        )
        self.wait(1)

        text2 = Text("State 0")
        text3 = Text("State 1")
        text4 = Text("State 2")
        text5 = Text("State 3")
        text6 = Text("State 4")
        text7 = Text("State 5")
        text8 = Text("State 6")

        camera_frame = self.camera.frame

        text2.scale(0.2)
        text3.scale(0.2)
        text4.scale(0.2)
        text5.scale(0.2)
        text6.scale(0.2)
        text7.scale(0.2)
        text8.scale(0.2)
        
        text2.move_to(camera_frame.get_center() + 1.1*LEFT + 0.7*UP)
    
        text3.next_to(text2, DOWN, buff=0.1)
        text4.next_to(text3, DOWN, buff=0.1)
        text5.next_to(text4, DOWN, buff=0.1)
        text6.next_to(text5, DOWN, buff=0.1)
        text7.next_to(text6, DOWN, buff=0.1)
        text8.next_to(text7, DOWN, buff=0.1)

        # STATE 0
        zero_text = Text("0").scale(0.2)
        zero_text.move_to(camera_frame.get_center())
        self.add(zero_text)
        arrow1 = Arrow(LEFT,RIGHT , tip_length = 0.2)
        arrow1.scale(0.4)
        arrow1.move_to(camera_frame.get_center() + 0.3*UP)
        arrow2 = Arrow(RIGHT,LEFT, tip_length = 0.2)
        arrow2.scale(0.4)
        arrow2.move_to(camera_frame.get_center() + 0.3*DOWN)
        self.play(Write(text2), Write(arrow1), Write(arrow2))
        
        car1 = Dot().set_color(ORANGE).move_to(number_plane.c2p(2, 3))
        car1.scale(0.5)
        car3 = Dot().set_color(ORANGE).move_to(number_plane.c2p(1.8, 3))
        car3.scale(0.5)
        car4 = Dot().set_color(ORANGE).move_to(number_plane.c2p(1.6, 3))
        car4.scale(0.5)
        
        self.add(car1)
        self.add(car3)
        self.add(car4)
        
        hor_path1 = Line(number_plane.c2p(2,3), number_plane.c2p(4,3))
        hor_path3 = Line(number_plane.c2p(1.8,3), number_plane.c2p(3.8,3))
        hor_path4 = Line(number_plane.c2p(1.6,3), number_plane.c2p(3.6,3))

        self.play(
            MoveAlongPath(car1, hor_path1), 
            MoveAlongPath(car3, hor_path3), 
            MoveAlongPath(car4, hor_path4), 
            run_time=2, 
            rate_func=linear,
            )
        
        self.remove(car1, car3, car4)
        

        car2 = Dot().set_color(ORANGE).move_to(number_plane.c2p(4, 3))
        self.add(car2)
        car2.scale(0.5)
        
        car5 = Dot().set_color(ORANGE).move_to(number_plane.c2p(4.2, 3))
        self.add(car5)
        car5.scale(0.5)

        car6 = Dot().set_color(ORANGE).move_to(number_plane.c2p(4.4, 3))
        self.add(car6)
        car6.scale(0.5)

        hor_path2 = Line(number_plane.c2p(4,3), number_plane.c2p(2,3))
        hor_path5 = Line(number_plane.c2p(4.2,3), number_plane.c2p(2.3,3))
        hor_path6 = Line(number_plane.c2p(4.4,3), number_plane.c2p(2.5,3))

        self.play(
            MoveAlongPath(car2, hor_path2), 
            MoveAlongPath(car5, hor_path5), 
            MoveAlongPath(car6, hor_path6), 
            run_time=2, 
            rate_func=linear
            )
        
        self.remove(car2, car5, car6)

        self.play(
            Unwrite(arrow1),
            Unwrite(arrow2)
        )

        self.remove(zero_text)

        self.wait(1)


        #STATE 1
        # Add vertical arrows
        arrow_up = Arrow(DOWN, UP, tip_length=0.2)
        arrow_up.scale(0.4)
        arrow_up.move_to(self.camera.frame.get_center() + 0.3*LEFT)

        arrow_down = Arrow(UP, DOWN, tip_length=0.2)
        arrow_down.scale(0.4)
        arrow_down.move_to(self.camera.frame.get_center() + 0.3*RIGHT)
        self.play(Write(text3), Write(arrow_up), Write(arrow_down))
        
                # Display the "1" label
        one_text = Text("1").scale(0.2)
        one_text.move_to(self.camera.frame.get_center())
        self.add(one_text)

        # Add dots (cars) moving vertically
        vehicle1 = Dot().set_color(BLUE).move_to(number_plane.c2p(3, 2))
        vehicle1.scale(0.5)
        vehicle2 = Dot().set_color(BLUE).move_to(number_plane.c2p(3, 1.8))
        vehicle2.scale(0.5)
        vehicle3 = Dot().set_color(BLUE).move_to(number_plane.c2p(3, 1.6))
        vehicle3.scale(0.5)

        self.add(vehicle1, vehicle2, vehicle3)

        # Define vertical paths
        ver_path1 = Line(number_plane.c2p(3, 2), number_plane.c2p(3, 4))
        ver_path2 = Line(number_plane.c2p(3, 1.8), number_plane.c2p(3, 3.8))
        ver_path3 = Line(number_plane.c2p(3, 1.6), number_plane.c2p(3, 3.6))

        self.play(
            MoveAlongPath(vehicle1, ver_path1), 
            MoveAlongPath(vehicle2, ver_path2), 
            MoveAlongPath(vehicle3, ver_path3), 
            run_time=2, 
            rate_func=linear
        )
        self.remove(vehicle1, vehicle2, vehicle3)

        # Add new dots (cars) for reverse direction
        vehicle4 = Dot().set_color(BLUE).move_to(number_plane.c2p(3, 4))
        vehicle4.scale(0.5)
        self.add(vehicle4)

        vehicle5 = Dot().set_color(BLUE).move_to(number_plane.c2p(3, 4.2))
        vehicle5.scale(0.5)
        self.add(vehicle5)

        vehicle6 = Dot().set_color(BLUE).move_to(number_plane.c2p(3, 4.4))
        vehicle6.scale(0.5)
        self.add(vehicle6)

        # Define reverse vertical paths
        ver_path4 = Line(number_plane.c2p(3, 4), number_plane.c2p(3, 2))
        ver_path5 = Line(number_plane.c2p(3, 4.2), number_plane.c2p(3, 2.2))
        ver_path6 = Line(number_plane.c2p(3, 4.4), number_plane.c2p(3, 2.4))

        self.play(
            MoveAlongPath(vehicle4, ver_path4), 
            MoveAlongPath(vehicle5, ver_path5), 
            MoveAlongPath(vehicle6, ver_path6), 
            run_time=2, 
            rate_func=linear
        )
        self.remove(vehicle4, vehicle5, vehicle6)

        self.play(
            Unwrite(arrow_up),
            Unwrite(arrow_down)
        )
        self.remove(one_text)

        self.wait(1)
        
        
        #STATE 2
         # Add adjusted arrows for the new motion
        arrow_rt1 = CurvedArrow(LEFT, DOWN, angle=-PI / 2, tip_length=0.2)
        arrow_rt1.scale(0.4)
        arrow_rt1.move_to(self.camera.frame.get_center() + 0.3*DOWN + 0.3*LEFT)

        arrow_rt2 = CurvedArrow(RIGHT, UP, angle=-PI / 2, tip_length=0.2)
        arrow_rt2.scale(0.4)
        arrow_rt2.move_to(self.camera.frame.get_center() + 0.3*UP + 0.3*RIGHT)

        arrow_rt3 = CurvedArrow(DOWN, RIGHT, angle=-PI / 2, tip_length=0.2)
        arrow_rt3.scale(0.4)
        arrow_rt3.move_to(self.camera.frame.get_center() + 0.3*DOWN + 0.3*RIGHT)

        arrow_rt4 = CurvedArrow(UP, LEFT, angle=-PI / 2, tip_length=0.2)
        arrow_rt4.scale(0.4)
        arrow_rt4.move_to(self.camera.frame.get_center() + 0.3*UP + 0.3*LEFT)


        self.play(Write(text4), Write(arrow_rt1), Write(arrow_rt2), Write(arrow_rt3), Write(arrow_rt4))
        
         # Display the "2" label
        two_text = Text("2").scale(0.2)
        two_text.move_to(self.camera.frame.get_center())
        self.add(two_text)

        # Add dots (cars) starting from the left side (moving to the middle, then down)
        car1 = Dot().set_color(PURPLE).move_to(number_plane.c2p(2, 3))
        car1.scale(0.5)

        self.add(car1)

        # Define two-segment paths for left-side cars
        lt_path1_part1 = Line(number_plane.c2p(2, 3), number_plane.c2p(3, 3))
        lt_path1_part2 = Line(number_plane.c2p(3, 3), number_plane.c2p(3, 2))

        self.play(
            MoveAlongPath(car1, lt_path1_part1),
            rate_func=linear,
            run_time=1
        )

        self.play(
            MoveAlongPath(car1, lt_path1_part2),
            rate_func=linear,
            run_time=1
        )
        self.remove(car1)

        # Add dots (cars) starting from the right side (moving to the middle, then up)
        car3 = Dot().set_color(PURPLE).move_to(number_plane.c2p(4, 3))
        car3.scale(0.5)

        self.add(car3)

        # Define two-segment paths for right-side cars
        rt_path3_part1 = Line(number_plane.c2p(4, 3), number_plane.c2p(3, 3))
        rt_path3_part2 = Line(number_plane.c2p(3, 3), number_plane.c2p(3, 4))

        self.play(
            MoveAlongPath(car3, rt_path3_part1),
            rate_func=linear,
            run_time=1
        )

        self.play(
            MoveAlongPath(car3, rt_path3_part2),
            rate_func=linear,
            run_time=1
        )
        self.remove(car3)

        self.play(
            Unwrite(arrow_rt1),
            Unwrite(arrow_rt2),
            Unwrite(arrow_rt3),
            Unwrite(arrow_rt4)
        )

        self.remove(two_text)

        self.wait(1)
        
        #STATE 3
         # Add the curved arrow (bottom to left)
        curved_arrow = CurvedArrow(DOWN, LEFT, angle=PI / 2, tip_length=0.2)
        curved_arrow.scale(0.4)
        curved_arrow.move_to(self.camera.frame.get_center() + 0.3*DOWN + 0.3*LEFT)
        self.play(Write(text5), Write(curved_arrow))

        # Display the "3" label
        three_text = Text("3").scale(0.2)
        three_text.move_to(self.camera.frame.get_center())
        self.add(three_text)

        # Add the car (Dot) at the starting position (bottom-center)
        car_state3 = Dot().set_color(RED).move_to(number_plane.c2p(3, 2))
        car_state3.scale(0.5)
        self.add(car_state3)

        # Define two-segment path: from the bottom to the middle, then to the left
        path1 = Line(number_plane.c2p(3, 2), number_plane.c2p(3, 3))  # Bottom to middle
        path2 = Line(number_plane.c2p(3, 3), number_plane.c2p(2, 3))  # Middle to left

        # Play the car animation along the two segments
        self.play(
            MoveAlongPath(car_state3, path1),
            rate_func=linear,
            run_time=1
        )
        self.play(
            MoveAlongPath(car_state3, path2),
            rate_func=linear,
            run_time=1
        )

        # Remove the car after it completes its motion
        self.remove(car_state3)

        self.play(Unwrite(curved_arrow))
        self.remove(three_text)
        self.wait(1)
       
        #STATE 4
        # Add the curved arrow (left to up)
        curved_arrow_4 = CurvedArrow(LEFT, UP, angle=PI / 2, tip_length=0.2)
        curved_arrow_4.scale(0.4)
        curved_arrow_4.move_to(self.camera.frame.get_center() + 0.3 * LEFT + 0.3 * UP)

        self.play(Write(text6),Write(curved_arrow_4))
        
         # Display the "4" label
        four_text = Text("4").scale(0.2)
        four_text.move_to(self.camera.frame.get_center())
        self.add(four_text)

        # Add the car (Dot) at the starting position (left-center)
        car_state4 = Dot().set_color(BLUE).move_to(number_plane.c2p(2, 3))
        car_state4.scale(0.5)
        self.add(car_state4)

        # Define two-segment path: from the left to the middle, then to the up
        path4_1 = Line(number_plane.c2p(2, 3), number_plane.c2p(3, 3))  # Left to middle
        path4_2 = Line(number_plane.c2p(3, 3), number_plane.c2p(3, 4))  # Middle to up

        # Play the car animation along the two segments
        self.play(
            MoveAlongPath(car_state4, path4_1),
            rate_func=linear,
            run_time=1
        )
        self.play(
            MoveAlongPath(car_state4, path4_2),
            rate_func=linear,
            run_time=1
        )

        # Remove the car after it completes its motion
        self.remove(car_state4)

        self.play(Unwrite(curved_arrow_4))
        self.remove(four_text)
        self.wait(1)
        
        #STATE 5
        # Add the curved arrow (right to down)
        curved_arrow_5 = CurvedArrow(RIGHT, DOWN, angle=PI / 2, tip_length=0.2)
        curved_arrow_5.scale(0.4)
        curved_arrow_5.move_to(self.camera.frame.get_center() + 0.3 * RIGHT + 0.3 * DOWN)

        self.play(Write(text7), Write(curved_arrow_5))
        
        # Display the "5" label
        five_text = Text("5").scale(0.2)
        five_text.move_to(self.camera.frame.get_center())
        self.add(five_text)

        # Add the car (Dot) at the starting position (right-center)
        car_state5 = Dot().set_color(GREEN).move_to(number_plane.c2p(4, 3))
        car_state5.scale(0.5)
        self.add(car_state5)

        # Define two-segment path: from the right to the middle, then to the down
        path5_1 = Line(number_plane.c2p(4, 3), number_plane.c2p(3, 3))  # Right to middle
        path5_2 = Line(number_plane.c2p(3, 3), number_plane.c2p(3, 2))  # Middle to down

        # Play the car animation along the two segments
        self.play(
            MoveAlongPath(car_state5, path5_1),
            rate_func=linear,
            run_time=1
        )
        self.play(
            MoveAlongPath(car_state5, path5_2),
            rate_func=linear,
            run_time=1
        )

        # Remove the car after it completes its motion
        self.remove(car_state5)

        self.play(Unwrite(curved_arrow_5))
        self.remove(five_text)
        self.wait(1)
        
        #STATE 6
        # Add the curved arrow (up to right)
        curved_arrow_6 = CurvedArrow(UP, RIGHT, angle=PI / 2, tip_length=0.2)
        curved_arrow_6.scale(0.4)
        curved_arrow_6.move_to(self.camera.frame.get_center() + 0.3 * UP + 0.3 * RIGHT)

        self.play(Write(text8), Write(curved_arrow_6))

        # Display the "6" label
        six_text = Text("6").scale(0.2)
        six_text.move_to(self.camera.frame.get_center())
        self.add(six_text)

        # Add the car (Dot) at the starting position (up-center)
        car_state6 = Dot().set_color(BLUE).move_to(number_plane.c2p(3, 4))
        car_state6.scale(0.5)
        self.add(car_state6)

        # Define two-segment path: from the up to the middle, then to the right
        path6_1 = Line(number_plane.c2p(3, 4), number_plane.c2p(3, 3))  # Up to middle
        path6_2 = Line(number_plane.c2p(3, 3), number_plane.c2p(4, 3))  # Middle to right

        # Play the car animation along the two segments
        self.play(
            MoveAlongPath(car_state6, path6_1),
            rate_func=linear,
            run_time=1
        )
        self.play(
            MoveAlongPath(car_state6, path6_2),
            rate_func=linear,
            run_time=1
        )

        # Remove the car after it completes its motion
        self.remove(car_state6)

        self.play(Unwrite(curved_arrow_6))
        self.remove(six_text)
        self.wait(1) 

        self.play(Unwrite(text2), 
                  Unwrite(text3), 
                  Unwrite(text4), 
                  Unwrite(text5), 
                  Unwrite(text6), 
                  Unwrite(text7),
                  Unwrite(text8), 
                  Unwrite(target_point)
                  )
        
        
        self.play(
            self.camera.frame.animate.set(width=19, height=10).move_to(ORIGIN)
        )


        self.play(FadeOut(brace1_lab), FadeOut(brace2_lab), FadeOut(number_plane), (FadeOut(dot) for dot in intersection), FadeOut(grid_border), FadeOut(brace1), FadeOut(brace2))

        # #DONT NEED THIS STUFF
        # # Download data and put in DataFrame
        # data_url = "https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/regression/linear_normal.csv"

        # df = pd.read_csv(data_url)

        # # Animate the creation of Axes
        # ax = Axes(x_range=[0, 100, 5], y_range=[-20, 200, 10])


        # self.play(Write(ax))

        # self.wait()  # wait for 1 second

        # # Animate the creation of dots
        # dots = [Dot(ax.c2p(x, y), color=BLUE) for x, y in df.values]
        # self.play(LaggedStart(*[Write(dot) for dot in dots], lag_ratio=.05))

        # self.wait()  # wait for 1 second


class BackgroundVideo (Scene):
    def construct():
        number_plane = NumberPlane(
            x_range=(1, 4, 1),
            y_range=(1, 4, 1),
            x_length=6,
            y_length=6,
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )

        number_plane.axes.set_opacity(0)

        intersectionsVal = {
            "x" : [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
            "y" : [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
        }
        
        dfinter = pd.DataFrame(intersectionsVal)
        
        # Calculate exact corner points for the border rectangle
        x_min, x_max = number_plane.x_range[0], number_plane.x_range[1]
        y_min, y_max = number_plane.y_range[0], number_plane.y_range[1]

        # Create a rectangle that aligns with the outermost grid lines
        grid_border = Polygon(
            number_plane.c2p(x_min, y_min),  # Bottom-left corner
            number_plane.c2p(x_max, y_min),  # Bottom-right corner
            number_plane.c2p(x_max, y_max),  # Top-right corner
            number_plane.c2p(x_min, y_max),  # Top-left corner
            color=TEAL,
            stroke_width=4
        )
        intersection = [Dot(number_plane.c2p  (x,y), color=BLUE) for x, y in dfinter.values]

        self.play(Write(grid_border))
        self.play(Write(number_plane))
        self.play(LaggedStart(*[Write(dot) for dot in intersection], lag_ratio=.05))
        
        self.wait(1)

        