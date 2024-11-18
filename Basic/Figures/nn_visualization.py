from manim import *

class NeuralNetworkVisualization(Scene):
    def construct(self):
        # Título de la escena
        title = Text("Visualización de red neuronal", font_size=36).to_edge(UP)
        self.play(Write(title))
        
        # Capas de la red neuronal
        input_neurons = VGroup(*[Circle(radius=0.2, color=BLUE).shift(UP * i * 0.7) for i in range(3)]).shift(LEFT * 4)
        hidden_layer_1 = VGroup(*[Circle(radius=0.2, color=GREEN).shift(UP * i * 0.7) for i in range(3)]).shift(LEFT * 2)
        hidden_layer_2 = VGroup(*[Circle(radius=0.2, color=ORANGE).shift(UP * i * 0.7) for i in range(3)])
        output_neurons = VGroup(*[Circle(radius=0.2, color=RED).shift(UP * i * 0.7) for i in range(2)]).shift(RIGHT * 2)

        # Añadir capas a la escena
        self.play(FadeIn(input_neurons, hidden_layer_1, hidden_layer_2, output_neurons))

        # Conexiones iniciales con pesos aleatorios
        connections = VGroup()
        weights = {}
        layers = [input_neurons, hidden_layer_1, hidden_layer_2, output_neurons]
        for l1, l2 in zip(layers[:-1], layers[1:]):
            for n1 in l1:
                for n2 in l2:
                    line = Line(n1.get_center(), n2.get_center(), stroke_width=2)
                    weight = DecimalNumber(0.5, num_decimal_places=2).scale(0.3).next_to(line.get_center(), UP)
                    weights[line] = weight
                    connections.add(line, weight)

        self.play(Create(connections))

        # Simulación del cambio de pesos en varias iteraciones
        for _ in range(5):
            self.wait(1)
            for line, weight in weights.items():
                new_weight = DecimalNumber(np.random.uniform(-1, 1), num_decimal_places=2).scale(0.3).move_to(weight.get_center())
                self.play(Transform(weight, new_weight), run_time=0.5)
        
        # Destacar la salida final
        output_highlight = SurroundingRectangle(output_neurons, color=YELLOW, buff=0.4)
        self.play(Create(output_highlight))
        self.wait(2)

        # Limpiar la escena
        self.play(FadeOut(connections, input_neurons, hidden_layer_1, hidden_layer_2, output_neurons, output_highlight, title))
