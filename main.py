from tkinter import *
import table, ball, bat

x_velocity = 10
y_velocity = 10

window = Tk()
window.title("MyPong")
       
my_table = table.Table(window, net_color="green", vertical_net=True)

my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=24, height=24, color="red", x_start=288, y_start=188)

bat_L = bat.Bat(table=my_table, width=15, height=100, x_posn=20, y_posn=150, color="blue")
bat_R = bat.Bat(table=my_table, width=15, height=100, x_posn=575, y_posn=150, color="yellow")


def game_flow():
    # 배트가 공을 받아치는지 확인:
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)
    
    my_ball.move_next()
    window.after(50, game_flow)

window.bind("a", bat_L.move_up)
window.bind("z", bat_L.move_down)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)

game_flow()

window.mainloop()
