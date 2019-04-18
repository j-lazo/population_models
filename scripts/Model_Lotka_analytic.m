clear all 
close all
clc

global alpha;
global beta_gr;
global beta_r;
global gamma_r;
global gamma_f;
global delta_r;
global delta_f;
global k_g;
global k_r;
global s_f;
global s_r;

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

% g0=500;
% r0=200;
% f0=110;
g0=150;
r0=150;
f0=150;

x0=[g0;r0;f0];

t0=0;
tmax=100;


[t Y]=ode45(@prey_pred_2,[t0,tmax],x0);

figure(1)
plot(t,Y(:,1),'g*-',t,Y(:,2),'bo-',t,Y(:,3),'r-+')
grid on
title('Population vs time')
legend('Prey','Predator 1','Preador 2')
xlabel('time steps')
ylabel('number of individuals')
pos1 = get(gcf, 'Position'); %// gives x left, y bottom, width, height
xx1=pos1(1);
yy1=pos1(2);
equis = pos1(3);
ye = pos1(4);
%htext=text(750,900,sprintf('\\alpha= %0.1g , \n \\gamma= %0.1g , \n \\delta= %0.1g, \n x_0= %0.1g \n y_0= %0.1g',alpha ,beta,gamma,delta,x0,y0),'FontSize',16);
dir=strcat(cd,'/results/');
save=strcat(dir,'/_lotkavolterra_ode45_',num2str(size),'_',num2str(g0),'_',num2str(r0),'_',num2str(f0),'.png');    
saveas(figure(1),save);

%%
 tplo=t;
 gplot=Y(:,1);
 rplot=Y(:,2);
 fplot=Y(:,3);


figure(2)
plot3(gplot,rplot,fplot,'-*')
grid on
xlabel('Number of Predators');
ylabel('Number of Preys');
title('Population Model');
pos1 = get(gcf, 'Position'); %// gives x left, y bottom, width, height
xx1=pos1(1);
yy1=pos1(2);
equis = pos1(3);
ye = pos1(4);
%htext=text(750,900,sprintf('\\alpha= %0.1g , \n \\gamma= %0.1g , \n \\delta= %0.1g, \n x_0= %0.1g \n y_0= %0.1g',alpha ,beta,gamma,delta,x0,y0),'FontSize',16);

save=strcat(dir,'/_lotkavolterra_ode45_spaceplot_',num2str(size),'_',num2str(g0),'_',num2str(r0),'_',num2str(f0),'.png');    
saveas(figure(2),save);
