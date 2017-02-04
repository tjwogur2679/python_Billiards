import table, random

# ball 클래스 정의
class Ball:
    # 초기화 메소드로 탁구공에 관한 변수 정의
    def __init__(self, table, width=14, height=14, color="red", x_speed=6, y_speed=4, x_start=0, y_start=0):
        self.width = width
        self.height = height
        self.x_posn = x_start
        self.y_posn = y_start
        self.color = color

        self.x_start = x_start
        self.y_start = y_start
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.circle = self.table.draw_oval(self)       
    
    # 탁구공의 시작 위치 메소드 정의
    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start
    # 탁구공 초기속도 메소드 정의
    def start_ball(self, x_speed, y_speed):
        self.x_speed = -x_speed if random.randint(0,1) else x_speed
        self.y_speed = -y_speed if random.randint(0,1) else y_speed
        self.start_position()
    # 탁구공의 움직임 메소드 정의
    def move_next(self):
        self.x_posn = self.x_posn + self.x_speed
        self.y_posn = self.y_posn + self.y_speed
        # 공이 왼쪽 벽에 부딪쳤을 때:
        if(self.x_posn <= 3):
            self.x_posn = 3
            self.x_speed = -self.x_speed
        # 공이 오른쪽 벽에 부딪쳤을 때:
        if(self.x_posn >= (self.table.width - (self.width - 3))):
            self.x_posn = (self.table.width - (self.width - 3))
            self.x_speed = -self.x_speed
        # 공이 위쪽 벽에 부딪쳤을 때:
        if(self.y_posn <= 3):
            self.y_posn = 3
            self.y_speed = -self.y_speed
        # 공이 아래쪽 벽에 부딪쳤을 때:
        if(self.y_posn >= (self.table.height - (self.height - 3))):
            self.y_posn = (self.table.height - (self.height - 3))
            self.y_speed = -self.y_speed
        # 마지막으로 원의 이동:
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)
    # 탁구공의 정지상태 메소드 정의
    def stop_ball(self):
        self.x_speed = 0
        self.y_speed = 0
