grammar Expr;

root : expr+ EOF;

expr :  PRINT (STRING| oper)
       | COLOR ID ',' '{' COLORES'}'
       | AREA oper
       | PERIMETER oper
       | VERTICES oper
       | CENTROID oper
       | EQUAL oper ',' oper
       | INSIDE oper ',' oper
       | DRAW STRING (',' ID)+
       | LINE_COMMENT EOF
       | ID ':=' oper;

oper : '#' oper
       |    oper (INTERSECT | UNION) oper
       |    '('oper')'
       | '[' NUMEROS
       | ID
       | '!' NUM;


COLORES: WS? FLOAT WS FLOAT WS FLOAT WS?;

PRINT : 'print';
COLOR : 'color';
AREA : 'area';
PERIMETER : 'perimeter';
VERTICES : 'vertices';
CENTROID : 'centroid';
EQUAL : 'equal';
INSIDE : 'inside';
DRAW : 'draw';
INTERSECT : '*';
UNION : '+';

LINE_COMMENT
: 
'//' ~[\r]*
;

STRING
:
 '"' ~'"'* '"'
;

ID
:
[A-Za-z_][A-Za-z0-9]*
;

NUMEROS :  ~(']'|'[')* ']';

POINT : NUM' 'NUM;

NUM : [0-9]+('.'[0-9]+)?;

FLOAT :   ('0'..'9')+ '.' ('0'..'9')*
      |   '.' ('0'..'9')+
      |   ('0'..'9')+
;


WS : [ \t\r\n] -> skip;
