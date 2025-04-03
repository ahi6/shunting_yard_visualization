from manim import * 
from manim_slides import Slide

height = 1
width = 1

# https://stackoverflow.com/a/70668543
def create_textbox(color, string):
    result = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        height=height, width=width, fill_color=color, 
        fill_opacity=0.3, stroke_color=color
    )
    text = Text(string).move_to(box.get_center()) # create text
    result.add(box, text) # add both objects to the VGroup
    return result



class DefaultTemplate(Slide):
    def construct(self):
        text = Text("1.5+2*(4-3)/5")
        self.play(Write(text))

        self.next_slide()

        squares = VGroup()
        prev = Text("")
        for i in ["1.5", "+", "2", "*", "(", "4", "-", "3", ")", "/", "5"]:
            textbox = create_textbox(WHITE, i)
            squares.add(textbox)
            textbox.next_to(prev, RIGHT)
            prev = textbox
        squares.center()
        self.play(Transform(text, squares))

        self.next_slide()

        main_stack = VGroup().add(Text("Hlavní zásobník", font_size=32).next_to(squares, DOWN))
        main_stack.align_to(squares, LEFT)
        main_stack.move_to(main_stack.get_center() + DOWN * 0.5)

        self.play(Create(main_stack))

        op_stack = VGroup().add(Text("Operátory").next_to(main_stack, DOWN))
        op_stack.align_to(main_stack, LEFT)
        op_stack.move_to(op_stack.get_center() + DOWN * 0.5)

        self.play(Create(op_stack))

        self.next_slide()

        def move_to_stack(stack, from_stack=squares, i=0, dest_i=-1):
            el = from_stack[i]
            dest = stack[dest_i].get_right() + RIGHT * 0.6
            line = Line(from_stack[i].get_center(), dest)
            from_stack.remove(el)

            self.clear()
            self.add(squares, main_stack, op_stack)
            self.play(MoveAlongPath(el, line))
            stack.add(el)
        
        def pop_from_stack(from_stack):
            el = from_stack[-1]
            self.play(Uncreate(el))
            from_stack.remove(el)

            self.clear()
            self.add(squares, main_stack, op_stack)

        move_to_stack(main_stack)
        move_to_stack(op_stack)
        move_to_stack(main_stack)
        move_to_stack(op_stack)
        move_to_stack(op_stack)
        move_to_stack(main_stack)
        move_to_stack(op_stack)
        move_to_stack(main_stack)
        move_to_stack(op_stack)
        pop_from_stack(op_stack)
        move_to_stack(main_stack, op_stack, -1)
        pop_from_stack(op_stack)
        move_to_stack(op_stack)
        move_to_stack(main_stack, op_stack, -2)
        move_to_stack(op_stack, op_stack, -1, -2)
        move_to_stack(main_stack)
        move_to_stack(main_stack, op_stack, -1)
        move_to_stack(main_stack, op_stack, -1)

        self.next_slide()
        
        self.remove(squares)

        self.play(Uncreate(main_stack[0]))
        main_stack.remove(main_stack[0])
        self.play(Uncreate(op_stack))

        def create_squares(from_stack):
            squares = VGroup()
            prev = Text("")
            for i in from_stack:
                i = i.copy()
                squares.add(i)
                i.next_to(prev, RIGHT)
                prev = i
            squares.center()
            return squares
        
        squares = create_squares(main_stack)
        self.play(Transform(main_stack, squares))

        self.next_slide()

        def pop(i=0, stack=squares):
            if isinstance(i, list):
                return pops(i, stack)

            el = stack[i]
            stack.remove(el)
            self.clear()
            self.add(stack)
            self.play(Uncreate(el))
            

            new = create_squares(stack)

            self.clear()
            self.play(Transform(stack, new))
            return new

        def pops(els=[0], stack=squares):
            els = [stack[i] for i in els]
 
            for el in els:
                stack.remove(el)
            
            self.clear()
            self.add(stack)

            els_group = VGroup()
            els_group.add(els)
            self.play(Uncreate(els_group))
            
            new = create_squares(stack)
            for _ in range(len(els)):
                new = create_squares(new)

            self.clear()
            self.play(Transform(stack, new))
            return new
        
        def highlight(i=0, stack=squares):
            el = stack[i]
            box = Rectangle(  # create a box
                height=height, width=width, fill_color=YELLOW_E, 
                fill_opacity=0.3, stroke_color=YELLOW_C
            )
            box.align_to(el, LEFT)
            return box

        def insert(text, i=0, stack=squares):
            el = create_textbox(WHITE, text)
            
            vgroup = VGroup()
            for j in range(i): # i cannot use slices because i don't want more vgroups
                vgroup.add(stack[j])
            vgroup.add(el)
            for j in range(i, len(stack)):
                vgroup.add(stack[j])
            new = create_squares(vgroup)

            self.clear()
            self.play(TransformMatchingShapes(stack, new))

            return new

        self.play(Create(h := highlight(0)))
        self.play(Uncreate(h))
        self.play(Create(h := highlight(1)))
        self.play(Uncreate(h))
        self.play(Create(h := highlight(2)))
        self.play(Uncreate(h))
        self.play(Create(h := highlight(3)))
        self.play(Uncreate(h))

        self.play(Create(h := highlight(4)))

        squares = pops([2, 3, 4], squares)
        squares = insert("1", 2, squares)

        self.play(Create(h := highlight(2, squares)))

        squares = pops([1, 2, 3], squares)
        squares = insert("2", 1, squares)

        self.play(Create(h := highlight(1, squares)))
        self.play(Uncreate(h))
        self.play(Create(h := highlight(2, squares)))
        self.play(Uncreate(h))
        self.play(Create(h := highlight(3, squares)))

        squares = pops([1, 2, 3], squares)
        squares = insert("0.4", 1, squares)

        self.play(Create(h := highlight(1, squares)))
        self.play(Uncreate(h))
        self.play(Create(h := highlight(2, squares)))
        squares = pops([0, 1, 2], squares)
        squares = insert("1.9", 0, squares)


        self.wait(5)




