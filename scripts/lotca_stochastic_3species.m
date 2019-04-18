function lotca_stochastic_3species();

clear all
close all
clc

%initial conditions 

global alpha
global beta_gr
global beta_r
global gamma_r
global gamma_f
global delta_r
global delta_f
global k_g
global k_r
global s_f
global s_r

size=50;

alpha=1;
beta_gr=1;
beta_r=1;

gamma_r=3;
gamma_f=4;

delta_r=1;
delta_f=1;

k_g=size^2;
k_r=size^2;

s_f=1;
s_r=1;


t0=0;
t=t0;
g0=150;
r0=150;
f0=150;

gplot=ones(1,1)*g0;
rplot=ones(1,1)*r0;
fplot=ones(1,1)*f0;
tplo=zeros(1,1);
tplo(1,1)=t0;


s=0;
smax=1000000;

g=g0;
r=r0;
f=f0;

while s<smax    
    
    a(1)=(alpha*(1-g/k_g))*g;
    a(2)=(beta_gr*(r/(k_g+g)))*g;
    a(3)=(gamma_r*(g/(k_g+g-s_r)))*r;
    a(4)=(beta_r*(f/(k_r+r)))*r;
    a(5)=delta_r*r;
    a(6)=(gamma_f*r/(k_r+r-s_f))*f;
    a(7)=(delta_f)*f;
    a0=sum(a);
    %step 2
    re=rand(2,1);
    tao=-log(re(1))/a0;
    mu=find((cumsum(a) >= re(2)*a0),1,'first');
    %step 3
    t=t+tao;
    
    if mu==1
        g=g+1;
    elseif mu==2
        g=g-1;        
    elseif mu==3
        r=r+1;
    elseif mu==4
        r=r-1;
    elseif mu==5
        r=r-1;
    elseif mu==6
        f=f+1;
    elseif mu==7
        f=f-1;
        
    end
   
 s=s+1;
 tplo(s)=t;
 gplot(s)=g;
 rplot(s)=r;
 fplot(s)=f;
 end
 
%plots and ode solver    

figure(1)    
%plot(tplo,Xplot,'*b',te,ex,'r');
plot(tplo,gplot,'g',tplo,rplot,'b',tplo,fplot,'r');
grid on
xlabel('time');
ylabel('Number of individuals');
title('Lotka-Voletrra Stochastic Model 3 species');
legend('Prey','Predator 1','Preador 2')
pos = get(gcf, 'Position'); %// gives x left, y bottom, width, height
equis = pos(3);
ye = pos(4);
%htext=text(equis/2,ye/2,sprintf('\\alpha= %0.1g , \n \\gamma= %0.1g , \n \\delta= %0.1g, \n x_0= %0.1g \n y_0= %0.1g',alpha ,beta,gamma,delta,x0,y0),'FontSize',16);
dir=strcat(cd,'/reulsts/');
save=strcat(dir,'_lotkavolterra_guillespie_',num2str(g0),'_',num2str(r0),'_',num2str(f0),'.png');  
saveas(figure(1),save);

figure(2)
plot3(gplot,rplot,fplot)
grid on
xlabel('Number of Predators');
ylabel('Number of Preys');
title('Lotka-Voletrra Stochastic Model');
pos1 = get(gcf, 'Position'); %// gives x left, y bottom, width, height
xx1=pos1(1);
yy1=pos1(2);
equis = pos1(3);
ye = pos1(4);
%htext=text(750,900,sprintf('\\alpha= %0.1g , \n \\gamma= %0.1g , \n \\delta= %0.1g, \n x_0= %0.1g \n y_0= %0.1g',alpha ,beta,gamma,delta,x0,y0),'FontSize',16);

save=strcat(dir,'/_lotkavolterra_guillespie_spaceplot_',num2str(size),'_',num2str(g0),'_',num2str(r0),'_',num2str(f0),'.png');    
saveas(figure(2),save);
end
