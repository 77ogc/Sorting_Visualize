import pygame
import random
import sys    
    
SIZE = 20
OFFSET = 5
BAR_X_LOCATION_DIFF = 30
BAR_X_GAP = 2
BAR_WIDTH = 20
red = (255, 20, 20)
blue = (20, 20, 255)
green = (20, 255, 20)
black = (0,0,0)

bubble = 'a : Bubble sort'
selection = 's : Selection sort'
insertion = 'd : Insertion sort'
merge = 'f : Merge sort'
quick = 'g : Quick sort'


class Visualizer():

    def __init__(self):
        self.rect_array = [ pygame.Rect( OFFSET + i * BAR_X_LOCATION_DIFF + i * BAR_X_GAP, 0, BAR_WIDTH, 400) for i in range(SIZE)]
        self.__init_window_utility()        
        self.__init_font()

    def __init_window_utility(self):
        pygame.init() 
        size = width, height = 640, 480
        self.background = black
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Visualizer")
        self.clock = pygame.time.Clock()      

    def __init_font(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        self.bubble = [font.render(bubble, False, green) , (30,410)]
        self.selection = [font.render(selection, False, green) , (220,410)]
        self.insertion = [font.render(insertion, False, green) , (430,410)]
        self.merge = [font.render(merge, False, green) , (30,440)]
        self.quick = [font.render(quick, False, green) , (220,440)]

    def __isGreater(self, i, j):

        return self.rect_array[i].height < self.rect_array[j].height

    def __swap_value(self, i, j):

        temp = self.rect_array[i].height
        self.rect_array[i].height = self.rect_array[j].height
        self.rect_array[j].height = temp

    def __shuffle(self):

        for index, rect in enumerate(self.rect_array):
            rect.height = random.randint(50, 400)


    def __show(self, text_location, time, i = None, j = None):

        pygame.time.delay(time)
        self.__draw_rect(i, j)
        self.screen.blit(text_location[0], text_location[1])
        pygame.display.update()

    def __draw_rect(self, i = None, j = None):

        self.screen.fill(self.background)

        for index, rect in enumerate(self.rect_array):
            if index == i: color = blue
            elif index == j: color = green 
            else: color = red
            pygame.draw.rect(self.screen, color, rect)

## --------------------------------------------------

    def __merge(self, front, mid, end):
        
        l = []
        r = []
        for i in range(front, mid + 1):
            l.append(self.rect_array[i].height)

        for i in range(mid + 1, end + 1):
            r.append(self.rect_array[i].height)
           
        l.append(1000)
        r.append(1000)
        lidx ,ridx = 0, 0

        for i in range(front, end + 1):
            if l[lidx] >= r[ridx]:
                self.rect_array[i].height = r[ridx]
                ridx += 1
            else:
                self.rect_array[i].height = l[lidx]
                lidx += 1

            self.__show(self.merge, 70, i)

    def merge_sort(self, front, end):

        if end > front:
            mid = int((end + front) / 2)
            self.merge_sort(front, mid)
            self.merge_sort(mid + 1, end)
            self.__merge(front, mid, end)

## -------------------------------------------------- 

    def insertion_sort(self):

        for i in range(SIZE):
            key = i
            j = i - 1
            while j >= 0:
                if not self.__isGreater(j, key):
                    self.__swap_value(j, key)
                    self.__show(self.insertion, 100, j, key)
                    key = j
                
                j -= 1          

## --------------------------------------------------          

    def selection_sort(self):

        for i in range(SIZE):
            minimum_index = i
            compare_index = i + 1

            while compare_index < SIZE:
                if not self.__isGreater(minimum_index, compare_index): minimum_index = compare_index
 
                compare_index += 1

            self.__swap_value(minimum_index, i)
            self.__show(self.selection, 150, minimum_index, i)

## --------------------------------------------------

    def bubble_sort(self):
        for i in range(0, SIZE):
            for j in range(0, SIZE):
                if self.__isGreater(i, j):
                    self.__swap_value(i, j)
                    self.__show(self.bubble, 70, i, j)

## --------------------------------------------------  

    def __partition(self, low, high):

        pivot = high
        index = low - 1

        for j in range(low, high):
            if self.__isGreater(j, high):
                index += 1
                self.__swap_value(index, j)
                self.__show(self.quick, 100, index, j)

        self.__swap_value(index + 1, high)
        self.__show(self.quick, 100, index + 1, high)

        return index + 1

    def quick_sort(self, low, high):
        if low < high:
            pivot = self.__partition(low, high)
            self.quick_sort(low, pivot - 1)
            self.quick_sort(pivot + 1, high) 

## --------------------------------------------------
 
    def run(self):

        while True:
            self.clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.__shuffle()
                        self.bubble_sort()
                    elif event.key == pygame.K_s:
                        self.__shuffle()
                        self.selection_sort()
                    elif event.key == pygame.K_d:
                        self.__shuffle()
                        self.insertion_sort()
                    elif event.key == pygame.K_f:
                        self.__shuffle()
                        self.merge_sort(0, SIZE - 1)
                    elif event.key == pygame.K_g:
                        self.__shuffle()
                        self.quick_sort(0, SIZE - 1)


            self.__draw_rect()
            self.screen.blit(self.bubble[0], self.bubble[1])
            self.screen.blit(self.selection[0], self.selection[1])
            self.screen.blit(self.insertion[0], self.insertion[1])
            self.screen.blit(self.merge[0], self.merge[1])
            self.screen.blit(self.quick[0], self.quick[1])
            pygame.display.update() 


vs = Visualizer()
vs.run()
