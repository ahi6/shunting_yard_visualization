run:
	manim -pqm main.py DefaultTemplate
run-gl:
	manim --renderer opengl -pqm main.py DefaultTemplate
render:
	manim main.py DefaultTemplate
html:
	manim-slides convert DefaultTemplate scene.html -ccontrols=true --one-file
pptx:
	manim-slides convert DefaultTemplate scene.pptx 

