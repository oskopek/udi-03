program translate_me;

const st:string = 'This is just a string!';
var st2:string[255];
var i, stlen:integer;

begin
    stlen := length(st);
    setlength(st2, stlen);
    for i:=1 to stlen do begin
        st2[i] := st[stlen-i+1];
    end;
    writeln(st2);
end.
