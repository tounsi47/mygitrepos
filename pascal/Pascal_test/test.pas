program calculator;
uses crt;

var
  a, b, x: integer;
  operation_mode: string;

begin
  clrscr;
  Write('Please give the A value: ');
  Readln(a);
  Write('Please give the B value: ');
  Readln(b);
  Write('Choose the operation mode (sum/difference): ');
  Readln(operation_mode);
  
  if operation_mode = 'sum' then
  begin
    x := a + b;
    Writeln('a + b = ', x);
  end
  else if operation_mode = 'difference' then
  begin
    x := a - b;
    Writeln('a - b = ', x);
  end
  else
    Writeln('Invalid operation mode');
end.
