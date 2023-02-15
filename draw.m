width=1 ;
%横线线宽 ;
y1=[0,118.214,106.967,133.02,110.36,140.23,76.926,143.239,85.894];
for i =1:2:17     
    x=[i-0.5*width,i+0.5*width];     
    y=[y1((i+1)/2),y1((i+1)/2)] ; 
    line(x,y,'Color',"#77AC30",'LineWidth',2) 
end 
for i=1:2:17     
    if i==17         
        continue     
    end     
    x=[i+0.5*width, i+2-0.5*width];     
    y=[y1((i+1)/2), y1((i+3)/2)] ;    
    line(x,y,'Color',"#77AC30",'LineWidth',0.5,'LineStyle','--')  
end