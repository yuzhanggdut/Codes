package date2num;

public class Date2num {
    public static void main(String[] args){
		  String Date = "三十一号";//输入日期格式为*年*月*日
	      System.out.println("原始汉字日期："+Date);
	      System.out.println("标准化日期："+formatStr(Date));
	}
	
	public static String formatStr(String str){
        StringBuffer sb = new StringBuffer();
        if(str.indexOf("年")!=-1&&str.indexOf("月")!=-1){//字符串中含有‘年’和‘月’
        	sb=yearStr(str);
            sb.append(monthStr(str));
            sb.append(dayStr(str));
        }
        if(str.indexOf('年')!=-1&&str.indexOf('月')==-1){//字符串中只有‘年’
        	sb=yearStr(str);
        }
        if(str.indexOf('月')!=-1&&str.indexOf("年")==-1){//字符串中含有‘月’或含有‘月’和‘日’, 不含‘年’
        	sb=monthStr(str);
        	sb.append(dayStr(str));
        }
        if((str.indexOf('日')!=-1||str.indexOf('号')!=-1)&&str.indexOf('月')==-1){//字符串中只含有‘日’或‘号’，不含‘月’
        	sb=singledayStr(str);
        }
        return sb.toString();
	}
	
	/**
     * 描述：将源字符串中的汉字格式化为数字
     * @param sign 源字符串中的字符
     * @return
     */
    public static char formatDigit(char sign){
       if(sign == '零')
           sign = '0';
       if(sign == '一')
           sign = '1';
       if(sign == '二')
           sign = '2';
       if(sign == '三')
           sign = '3';
       if(sign == '四')
           sign = '4';
       if(sign == '五')
           sign = '5';
       if(sign == '六')
           sign = '6';
       if(sign == '七')
           sign = '7';
       if(sign == '八')
           sign = '8';
       if(sign == '九')
           sign = '9';
       return sign;
   }
   
   /**
    * 描述： 获得月份字符串的长度
    * @param str  待转换的源字符串
    * @param pos1 '年'的位置
    * @param pos2 '月'的位置
    * @return
    */
    public static int getMidLen(String str,int pos1,int pos2){
	  //System.out.println("月份的位数："+str.substring(pos1+1, pos2).length());
        return str.substring(pos1+1, pos2).length();
     }
  
  /**
   * 描述：获得日期字符串的长度
   * @param str  待转换的源字符串
   * @param pos2 '月'的位置
   * @return
   */
    public static int getLastLen(String str,int pos2){
	 //System.out.println("日的位数："+(str.substring(pos2+1).length()-1));
       if(str.indexOf('日')!=-1||str.indexOf('号')!=-1){//输入后缀为'日'或者'号'做减1；没有不减1.
    	   return (str.substring(pos2+1).length()-1);
       }
       else{
    	   return str.substring(pos2+1).length();
       }
   }
    
    public static int getLength(String str){
    	 //System.out.println("日的位数："+(str.length()-1));
       	 return (str.length()-1);
          
      }
    
    public static StringBuffer yearStr(String str){
   	 StringBuffer year = new StringBuffer();
   	 int pos1 = str.indexOf("年");
   	 for(int i = 0; i < pos1; i++){
         year.append(formatDigit(str.charAt(i)));//取单个字符转换并拼接
     }
         year.append('年');  
         return year;
    }
    
    public static StringBuffer monthStr(String str){
   	 StringBuffer month = new StringBuffer();
   	int pos1 = str.indexOf("年");
    int pos2 = str.lastIndexOf("月");
   	if(getMidLen(str,pos1,pos2) == 1){
    	if(str.charAt(pos1+1)=='十'){
    		month.append("10"+"月");
    	}	
    	else{
    		month.append(formatDigit(str.charAt(pos1+1))+"月");
    	}
    	
    }
    if(getMidLen(str,pos1,pos2) == 2){
    	for(int i = pos1+1; i < pos2; i++){
    		if(str.charAt(i)=='十'){
    			month.append("1");
        	}
    		else{
    			month.append(formatDigit(str.charAt(i)));
    		}
        }
    	month.append('月');
        
    }
        return month;
    }
    
    public static StringBuffer dayStr(String str){
      	StringBuffer day = new StringBuffer();
        int pos2 = str.lastIndexOf("月");
      	if(getLastLen(str,pos2) == 1){
        	if(str.charAt(pos2+1)=='十'){
        		day.append("10"+"日");
        	}	
        	else{
        		day.append(formatDigit(str.charAt(pos2+1))+"日");
        	}
        	
        }
        if(getLastLen(str,pos2) == 2){
        	//日期第一位
        	if(str.charAt(pos2+1)=='十'){
        		day.append("1");
        	}
        	else{
        		day.append(formatDigit(str.charAt(pos2+1)));
        	}
        	//日期第二位
        	if(str.charAt(pos2+2)=='十'){
        		day.append("0"+"日");
        	}
        	else{
        		day.append(formatDigit(str.charAt(pos2+2))+"日");
        	}
            
        }
        if(getLastLen(str,pos2) == 3){
        	for(int i = pos2+1; i < pos2+4; i++){
        		if(str.charAt(i)=='十'){
            		day.append("");
            	}
            	else{
            		day.append(formatDigit(str.charAt(i)));
            	}
        	}
        	day.append('日');
        }
           return day;
       }
    
    public static StringBuffer singledayStr(String str){
      	StringBuffer singleday = new StringBuffer();
      	if(getLength(str) == 1){
        	if(str.charAt(0)=='十'){
        		singleday.append("10"+"日");
        	}	
        	else{
        		singleday.append(formatDigit(str.charAt(0))+"日");
        	}
        	
        }
        if(getLength(str) == 2){
        	//日期第一位
        	if(str.charAt(0)=='十'){
        		singleday.append("1");
        	}
        	else{
        		singleday.append(formatDigit(str.charAt(0)));
        	}
        	//日期第二位
        	if(str.charAt(1)=='十'){
        		singleday.append("0"+"日");
        	}
        	else{
        		singleday.append(formatDigit(str.charAt(1))+"日");
        	}
            
        }
        if(getLength(str) == 3){
        	for(int i = 0; i < 3; i++){
        		if(str.charAt(i)=='十'){
        			singleday.append("");
            	}
            	else{
            		singleday.append(formatDigit(str.charAt(i)));
            	}
        	}
        	singleday.append('日');
        }
           return singleday;
       }
   
}
