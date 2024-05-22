# PingPong Game

#setup ball
ball_x, ball_y = 300, 200
ball_dx, ball_dy = 3, 3
ball_radius = 10

#setup paddle
paddle_width, paddle_height = 10, 60
left_paddle_y, right_paddle_y = 150, 150
paddle_speed = 5

#setup score 
left_score, right_score = 0, 0
max_score = 10

#setup canvas
def setup():
    size(600, 400)
    textSize(32)
    noStroke()
    
#setup draw
def draw():

    global ball_x, ball_y, ball_dx, ball_dy
    global left_paddle_y, right_paddle_y, left_score, right_score

    background(0)
    rect(300, 0, 10, 400)
    fill(255)
    
# setup who wins
    if left_score == max_score or right_score == max_score:
        fill(255)
        text("Left Wins!" if left_score == max_score else "Right Wins!", 180, 200)
        noLoop()
        return
    
#setup move balls
    ball_x += ball_dx
    ball_y += ball_dy

#setup ball collision
    if ball_y < ball_radius or ball_y > height - ball_radius:
        ball_dy *= -1

    if (ball_x - ball_radius < 40 and left_paddle_y < ball_y < left_paddle_y + paddle_height) or (
        ball_x + ball_radius > 560 and right_paddle_y < ball_y < right_paddle_y + paddle_height):
        ball_dx *= -1
        
#setup increment
    if ball_x < 0:
        right_score += 1
        reset_ball()

    if ball_x > width:
        left_score += 1
        reset_ball()
        
#setup color
    fill(255)
    ellipse(ball_x, ball_y, ball_radius * 2, ball_radius * 2)
    rect(30, left_paddle_y, paddle_width, paddle_height)
    rect(560, right_paddle_y, paddle_width, paddle_height)
    text(left_score, 150, 50)
    text(right_score, 450, 50)
    
#setup the keyboard
    if keyPressed:
        if key == 'w' and left_paddle_y > 0:
            left_paddle_y -= paddle_speed
        elif key == 's' and left_paddle_y < height - paddle_height:
            left_paddle_y += paddle_speed
        if keyCode == UP and right_paddle_y > 0:
            right_paddle_y -= paddle_speed
        elif keyCode == DOWN and right_paddle_y < height - paddle_height:
            right_paddle_y += paddle_speed
            
#setup playagain
def reset_ball():
    global ball_x, ball_y, ball_dx
    ball_x, ball_y = width // 2, height // 2
    ball_dx *= -1
