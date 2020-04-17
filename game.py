import pygame
import random as rand
import sys

def play_game():
  pygame.init()

  WIDTH = 800
  HEIGHT = 600
  RED = (255,0,0)
  BLUE = (0,0,255)
  YELLOW = (255,255,0)
  BACKGROUND_COLOR = (0,0,0)
  PLAYER_COLOR = BLUE
  ENEMIES_COLOR = RED
  STAR_COLOR = YELLOW

  player_size = 50
  player_pos = [WIDTH/2,HEIGHT-2*player_size]

  enemies_size = 50
  enemies_pos = [rand.randint(0,WIDTH-enemies_size),0]
  enemies_list = [enemies_pos]

  star_size = 20
  star_pos = [rand.randint(0,WIDTH-star_size),0]
  star_list = [star_pos]



  SPEED = 30

  screen = pygame.display.set_mode((WIDTH,HEIGHT))

  game_over = False

  clock = pygame.time.Clock()

  def drop_enemies(enemies_list):
    random = rand.randint(0,9)
    if len(enemies_list) < 5 and random > 4:
      xpos = rand.randint(0,WIDTH-enemies_size)
      ypos = 0
      
      enemies_list.append([xpos,ypos])

  def drop_stars(star_list):
    if len(star_list) < 1:
      xpos = rand.randint(0,WIDTH-star_size)
      ypos = 0
      
      star_list.append([xpos,ypos])

  #Draw Functions
  def draw_enemies(enemies_list):
    for enemies_pos in enemies_list:
      pygame.draw.rect(screen,ENEMIES_COLOR,(enemies_pos[0],enemies_pos[1],enemies_size,enemies_size))

  def draw_stars(star_list):
    for star_pos in star_list:
      pygame.draw.rect(screen,STAR_COLOR,(star_pos[0],star_pos[1],star_size,star_size))


  def detect_collision(player_pos,entity_pos,size):
    p_x = player_pos[0]
    p_y = player_pos[1]

    f_x = entity_pos[0]
    f_y = entity_pos[1]

    if (f_x >= p_x and f_x < (p_x + player_size)) or (p_x >= f_x and p_x < (f_x + size)):
      if (f_y >= p_y and f_y < (p_y + player_size)) or (p_y >= f_y and p_y < (f_y + size)):
        return True

    return False

  def collision_check(player_pos,entity_list,entity_size):
    for idx,pos in enumerate(entity_list):
      if detect_collision(player_pos,pos,entity_size):
        entity_list.pop(idx)
        return True
    return False

  # Move/Remove Enemies & Stars
  def update_enemies_positions(enemies_list):
    for idx, enemies_pos in enumerate(enemies_list):
      if enemies_pos[1] >= 0 and enemies_pos[1] < HEIGHT:
        enemies_pos[1] += 20
      else:
        enemies_list.pop(idx)

  def update_star_position(star_list):
    for idx, star_pos in enumerate(star_list):
      if star_pos[1] >= 0 and star_pos[1] < HEIGHT:
        star_pos[1] += 15
      else:
        star_list.pop(idx)


  score = 0

  while not game_over:
    for event in pygame.event.get():
      """
      This gets the user's input
      """
      if event.type == pygame.QUIT:
        sys.exit()

      if event.type == pygame.KEYDOWN:

        x = player_pos[0]
        y = player_pos[1]

        if event.key == pygame.K_LEFT:
          x -= player_size/2
        elif event.key == pygame.K_RIGHT:
          x += player_size/2

        player_pos = [x,y]


    screen.fill(BACKGROUND_COLOR)

    update_enemies_positions(enemies_list)
    update_star_position(star_list)


    if(collision_check(player_pos,enemies_list,enemies_size)):
      game_over = True
      break

    if(collision_check(player_pos,star_list,star_size)):
      score += 1

    # Draw actors
    drop_enemies(enemies_list)
    draw_enemies(enemies_list)

    drop_stars(star_list)
    draw_stars(star_list)

    pygame.draw.rect(screen,PLAYER_COLOR,(player_pos[0],player_pos[1],player_size,player_size))
    
    clock.tick(SPEED)

    pygame.display.update()

  return score