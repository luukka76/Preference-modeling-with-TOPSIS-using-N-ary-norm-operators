% Mainfiles purpose is to show how to use n-ary TOPSIS method
% that uses n-ary norm operators to set preference for either positive
% ideal solution or negative ideal solution depending on the practical
% problem. It was published in

% P. Luukka, N—ary norm operators and TOPSIS, 2020 IEEE International 
% Conference on Fuzzy Systems (FUZZ-IEEE), Glasgow, UK, 2020, pp. 1-6, 
% doi: 10.1109/FUZZ48607.2020.9177580.


%First lets create artificial data of ten alternatives and five criteria:
c=10;
data=c*randn(10,5);
%Define parameters p for Minkowski metric (1=Manhattan distance,2=Euclidean distance etc)
%and parameter values for fuzzy union (w) and intersection (w2) operators
p=1;  w=2; w2=5;
%See more information about these from the proceedings.

%Define whether criteria is benefit criteria or cost criteria in crit
%vector 1=benefit, 2=cost.
crit=[1 1 1 2 1]; %in this example fourth would be cost criteria and others benefit

[cc,PISB,NISB]=narytopsis(data,p,w,w2,crit)

%For output of the function you get:
%cc = closeness coefficient values for ten alternatives
%PISB = distance to positive ideal solution
%NISB = distance to negative ideal solution 

%You can get the ordering of the alternatives by sorting CC to descending order
[Y,I]=sort(cc,'descend');

%Order of the attributes:
Order=I'