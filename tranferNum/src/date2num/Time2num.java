package date2num;

public class Time2num {
    public static void main(String[] args){
		  String Date = "十二时三十五分二十九秒";//输入时间格式*时*分*秒
	      System.out.println("原始汉字时间："+Date);
	      System.out.println("标准化时间："+formatStr(Date));
	}
	
	public static String formatStr(String str){
        StringBuffer sb = new StringBuffer();
        sb=hourStr(str);
        sb.append(minuteStr(str));
        sb.append(secondStr(str));
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
    * 描述： 获得分位字符串的长度
    * @param str  待转换的源字符串
    * @param pos1 '时'的位置
    * @param pos2 '分'的位置
    * @return
    */
    public static int getMidLen(String str,int pos1,int pos2){
        return str.substring(pos1+1, pos2).length();
     }
  
  /**
   * 描述：获得秒位字符串的长度
   * @param str  待转换的源字符串
   * @param pos2 '分'的位置
   * @return
   */
    public static int getLastLen(String str,int pos2){
       return (str.substring(pos2+1).length()-1);//输入后缀为'秒'做减1；没有不减1.
   }
    
    /**
     * 描述： 获得时位字符串的长度
     * @param str  待转换的源字符串
     * @param pos1 '时'的位置
     * @return
     */
     public static int getStaLen(String str,int pos1){
         return str.substring(0, pos1).length();
      }
     
     /**
      * 描述：时位汉字转换成数字
      * @param str  待转换的源字符串
      * @param pos1 '时'的位置
      * @return
      */
     public static StringBuffer hourStr(String str){
    	 StringBuffer hour = new StringBuffer();
    	 int pos1 = str.indexOf("时");
         if(getStaLen(str,pos1) == 1){
         	if(str.charAt(0)=='十'){
         		hour.append("10"+":");
         	}	
         	else{
         		hour.append(formatDigit(str.charAt(0))+":");
         	}
         	
         }
         if(getStaLen(str,pos1) == 2){
         	if(str.charAt(0)=='十'){
         		hour.append("1");
         	}
         	else{
         		hour.append(formatDigit(str.charAt(0)));
         	}
         	if(str.charAt(1)=='十'){
         		hour.append("0"+":");
         	}
         	else{
         		hour.append(formatDigit(str.charAt(1))+":");
         	}
             
         }
         if(getStaLen(str,pos1) == 3){
         	for(int i = 0; i < pos1; i++){
         		if(str.charAt(i)=='十'){
         			hour.append("");
             	}
             	else{
             		hour.append(formatDigit(str.charAt(i)));
             	}
         	}
         	hour.append(':');
         }
         return hour;
     }
     
     /**
      * 描述：分位汉字转换成数字
      * @param str  待转换的源字符串
      * @param pos1 '时'的位置
      * @param pos2 '分'的位置
      * @return
      */
     public static StringBuffer minuteStr(String str){
    	 StringBuffer minute = new StringBuffer();
    	 int pos1 = str.indexOf("时");
         int pos2 = str.lastIndexOf("分");
         if(getMidLen(str,pos1,pos2) == 1){
         	if(str.charAt(pos1+1)=='十'){
         		minute.append("10"+":");
         	}	
         	else{
         		minute.append(formatDigit(str.charAt(pos1+1))+":");
         	}
         	
         }
         if(getMidLen(str,pos1,pos2) == 2){
         	if(str.charAt(pos1+1)=='十'){
         		minute.append("1");
         	}
         	else{
         		minute.append(formatDigit(str.charAt(pos1+1)));
         	}
         	if(str.charAt(pos1+2)=='十'){
         		minute.append("0"+":");
         	}
         	else{
         		minute.append(formatDigit(str.charAt(pos1+2))+":");
         	}
             
         }
         if(getMidLen(str,pos1,pos2) == 3){
         	for(int i = pos1+1; i < pos2; i++){
         		if(str.charAt(i)=='十'){
         			minute.append("");
             	}
             	else{
             		minute.append(formatDigit(str.charAt(i)));
             	}
         	}
         	minute.append(':');
         }
         return minute;
     }
     
     /**
      * 描述：秒位汉字转换成数字
      * @param str  待转换的源字符串
      * @param pos2 '分'的位置
      * @return
      */
     public static StringBuffer secondStr(String str){
    	 StringBuffer second = new StringBuffer();
         int pos2 = str.lastIndexOf("分");
         if(getLastLen(str,pos2) == 1){
         	if(str.charAt(pos2+1)=='十'){
         		second.append("10");
         	}	
         	else{
         		second.append(formatDigit(str.charAt(pos2+1)));
         	}
         	
         }
         if(getLastLen(str,pos2) == 2){
         	if(str.charAt(pos2+1)=='十'){
         		second.append("1");
         	}
         	else{
         		second.append(formatDigit(str.charAt(pos2+1)));
         	}
         	if(str.charAt(pos2+2)=='十'){
         		second.append("0");
         	}
         	else{
         		second.append(formatDigit(str.charAt(pos2+2)));
         	}
             
         }
         if(getLastLen(str,pos2) == 3){
         	for(int i = pos2+1; i < pos2+4; i++){
         		if(str.charAt(i)=='十'){
         			second.append("");
             	}
             	else{
             		second.append(formatDigit(str.charAt(i)));
             	}
         	}
         }
         return second;
     }
   
}
