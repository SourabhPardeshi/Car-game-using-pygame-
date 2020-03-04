def instruction():
    while True:
        game_display.fill(white)
        load_image(0,0,'images/bg.jpg')
        
        
        TextFont = pygame.font.SysFont("Times New Roman",50) #Stores Text font and its size    
        textSurf, textRect = text_object("WELCOME TO INSTRUCTIONS !",TextFont)
        textRect.center = ((display_width/2,display_height/5))
        game_display.blit(textSurf,textRect)

        load_image(150,200,'images/LeftArrow.png')
        load_image(300,200,'images/RightArrow.png')
        button("Start ",150,450,150,50, green, bright_green, game_loop)
        button("Quit ",350,450,150,50, red, bright_red, quitgame)
        

        pygame.display.update()
        clock.tick(15)

        
        #GAME INTRO

        button("Start !",150,250,150,50, green, bright_green, game_loop)
        button("Quit !",150,450,150,50, red, bright_red, quitgame)
        button("Instruction !",150,350,150,50, yellow, bright_yellow, instruction)
