from tkinter import *
import table, ball, bat

# 탁구공 속도 설정(전역변수)
x_velocity = 10
y_velocity = 10

# tkinter 라이브러리 사용 설정
window = Tk()
# 윈도우 캡션 이름 설정
window.title("MyPong")
# table 네트 설정
my_table = table.Table(window, net_color="green", vertical_net=True)
# 탁구공 설정
my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=24, height=24, color="red", x_start=288, y_start=188)
# 탁구채 설정
bat_L = bat.Bat(table=my_table, width=15, height=100, x_posn=20, y_posn=150, color="blue")
bat_R = bat.Bat(table=my_table, width=15, height=100, x_posn=575, y_posn=150, color="yellow")

# 메소드 정의
def game_flow():
    # 배트가 공을 받아치는지 확인:
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)
    # 탁구공 움직임 설정
    my_ball.move_next()
    # 게임 속도 설정
    window.after(50, game_flow)
# 게임 조작키 설정
window.bind("a", bat_L.move_up)
window.bind("z", bat_L.move_down)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)
# 메소드 호출
game_flow()
# 메인 루프 설정
window.mainloop()
