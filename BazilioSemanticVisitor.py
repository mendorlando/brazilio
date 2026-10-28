
from BazilioVisitor import BazilioVisitor


class BazilioSemanticVisitor(BazilioVisitor):

    def __init__(self):
        self.notas_midi = []
        self.errores = 0
        self.octava_base = 4

    def visitElemento(self, ctx):

        if ctx.SILENCIO() is not None:
            self.notas_midi.append(-1)
            print("Silencio musical")
            return None

        nota = ctx.NOTA().getText()

        nombre = nota[0]
        posicion = 1
        alteracion = 0

        if posicion < len(nota):
            if nota[posicion] == "#":
                alteracion = 1
                posicion += 1
            elif nota[posicion] == "b":
                alteracion = -1
                posicion += 1

        octava = self.octava_base

        if posicion < len(nota):
            octava = int(nota[posicion:])

        semitonos = {
            "C": 0,
            "D": 2,
            "E": 4,
            "F": 5,
            "G": 7,
            "A": 9,
            "B": 11
        }

        midi = (
            (octava + 1) * 12
            + semitonos[nombre]
            + alteracion
        )

        if midi < 21 or midi > 108:
            self.errores += 1
            print(
                f"Error semántico: {nota} "
                "fuera del rango del piano"
            )
            return None

        frecuencia = 440 * (2 ** ((midi - 69) / 12))

        self.notas_midi.append(midi)

        print(
            f"Nota: {nota:<4} | "
            f"MIDI: {midi:3d} | "
            f"Frecuencia: {frecuencia:.2f} Hz"
        )

        return None
