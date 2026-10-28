
grammar Bazilio;

// Programa principal
programa
    : MAIN LLAVE_ABRE elemento* LLAVE_CIERRA EOF
    ;

// Elementos musicales
elemento
    : NOTA
    | SILENCIO
    ;

// Palabras reservadas
MAIN : 'Main';

// Símbolos
LLAVE_ABRE : '{';
LLAVE_CIERRA : '}';

// Notas musicales:
// C4, D4, F#4, Bb4, C, E, etc.
NOTA
    : [A-G] [#b]? [0-8]?
    ;

// Silencio
SILENCIO : 'R';

// Ignorar espacios y saltos de línea
WS : [ \t\r\n]+ -> skip;
