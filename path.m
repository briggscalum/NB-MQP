clc
clear all
close 
syms y(x) x real
d=0.5
y=2*sin(x);
%y=sqrt(25-(x*x))
%y=2*x

dy=diff(y,x);
dyy=diff(dy,x);
X=[];
Y=[];
X1=[];
Y1=[];
X2=[];
Y2=[];


for i=-5:0.1:5
    xi=i;
    yi=subs(y,{x},{xi});
    X=[X;xi];
    Y=[Y;yi];
    tangent=subs(dy,{x},{xi});
    double_diff=subs(dyy,{x},{xi});
    m=-1*(1/tangent);
    normal=m*(x-xi)+yi;
%     if tangent==0
%         x1=xi;
%         y1=yi+10;
%         x2=xi;
%         y2=yi-10;
%    if double_diff>0
        if tangent>0
            x1=xi+(d/sqrt(1+(m*m)));
            x2=xi-(d/sqrt(1+(m*m)));
            y1=subs(normal,{x},{x1});
            y2=subs(normal,{x},{x2});
        elseif tangent<0
            x1=xi-(d/sqrt(1+(m*m)));
            x2=xi+(d/sqrt(1+(m*m)));
            y1=subs(normal,{x},{x1});
            y2=subs(normal,{x},{x2});
        elseif tangent==0
            x1=xi;
            y1=yi-d;
            x2=xi;
            y2=yi+d;            
        end
% 
%     elseif double_diff<0
%         if tangent>0
%             x1=xi-(d/sqrt(1+(m*m)));
%             x2=xi+(d/sqrt(1+(m*m)));
%             y1=subs(normal,{x},{x1});
%             y2=subs(normal,{x},{x2});
%         elseif tangent<0
%             x1=xi+(d/sqrt(1+(m*m)));
%             x2=xi-(d/sqrt(1+(m*m)));
%             y1=subs(normal,{x},{x1});
%             y2=subs(normal,{x},{x2});
%         elseif tangent==0
%             x1=xi;
%             y1=yi+d;
%             x2=xi;
%             y2=yi-d;
%             
%         end
%        
%     end
 
    X1=[X1;x1];
    Y1=[Y1;y1];
    X2=[X2;x2];
    Y2=[Y2;y2];
    
end
figure()
plot(X,Y,'color','r');
hold on;

plot(X1,Y1,'color','b');
hold on;

plot(X2,Y2,'color','g');
hold on;

axis([-5 5 -3 3])
% plot(X,Y,'g',X1,Y1,'b',X2,Y2,'r')
vpa(X1)









