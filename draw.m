width=1 ;
%横线线宽 ;
y1=[0,118.214,106.967,133.02,110.36,140.23,76.926,143.239,85.894];
y2=[0,73.834,37.561, 125.125 ,-1.4, 120.207 ,40.615 ,130.407 ,115.707 ];
y3=[0 73.834 37.561 125.125 -1.4 114.935 89.624 ];
xlabel('reaction coordinate')
ylabel('E(kcal/mol)')

%line1
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
%line2 begins below
for i =1:2:17          
    x=[i-0.5*width,i+0.5*width];          
    y=[y2((i+1)/2),y2((i+1)/2)] ;      
    line(x,y,'Color',"#EDB120",'LineWidth',2)  
end  
for i=1:2:17          
    if i==17                  
        continue          
    end          
    x=[i+0.5*width, i+2-0.5*width];          
    y=[y2((i+1)/2), y2((i+3)/2)] ;         
    line(x,y,'Color',"#EDB120",'LineWidth',0.5,'LineStyle','--')   
end
%line3
for i =1:2:13
    x=[i-0.5*width,i+0.5*width];  
    y=[y3((i+1)/2),y3((i+1)/2)] ; 
    line(x,y,'Color',[0,0.4470,0.7410,0.75],'LineWidth',2)  
end  
for i=1:2:13              
    if i==13                           
        continue              
    end               
    x=[i+0.5*width, i+2-0.5*width];              
    y=[y3((i+1)/2), y3((i+3)/2)] ;              
    line(x,y,'Color',[0,0.4470,0.7410,0.75],'LineWidth',0.5,'LineStyle','--')   
end
set(gca,'XTickLabel',[]); 
set(gca,'XTick',[]);