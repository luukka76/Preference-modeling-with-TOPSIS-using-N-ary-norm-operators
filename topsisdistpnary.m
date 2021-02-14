function [c,Dplus,Dminus,PIS,NIS,a]=topsis(data,p,w)
x=data;
[m,n]=size(x);
a=zeros(m,n);
%Normalization:
a=normalization2(x);

%Positive and negative ideal solutions:
PIS=zeros(1,n);
NIS=zeros(1,n);
w2=2;
for j=1:n
%    PIS(j)=max(a(:,j));
%    NIS(j)=min(a(:,j));
%    PIS(j)=tconormstandardn(a(:,j));
%    PIS(j)=tconormprob(a(:,j)');
%    PIS(j)=tconormluka(a(:,j)');
%    PIS(j)=tconormdrastic(a(:,j)');
    PIS(j)=recursivetconorm(a(:,j)',w);

    NIS(j)=recursivetnorm(a(:,j),w2);
%    NIS(j)=tnormstandardn(a(:,j));
%    NIS(j)=tnormprob(a(:,j)');
%    NIS(j)=tnormluka(a(:,j)');
end

%Distances to PIS and NIS
 DPISB=zeros(1,m);
 DNISB=zeros(1,m);
% m1=1;
% q=1;
%p=2;
for i=1:m
   Dplus(i)=distM(PIS,a(i,:),p); 
   Dminus(i)=distM(NIS,a(i,:),p); 
end
%Closeness coefficient: 
 c=zeros(1,m);
 for i=1:m
%     c(i)=DNIS(i)/(DPIS(i)+DNIS(i));
     c(i)=Dminus(i)/(Dplus(i)+Dminus(i));
 end
