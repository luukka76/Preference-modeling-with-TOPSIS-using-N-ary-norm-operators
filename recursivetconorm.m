function unorm=tconormstandardn(A,w)
[n,m]=size(A);
unorm=u_yager(A(1),A(2),w);
for i=2:n
    unorm=u_yager(A(i),unorm,w);
end
