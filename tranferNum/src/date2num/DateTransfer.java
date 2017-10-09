package date2num;

import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DateTransfer {
	private static final Map<String, String> chineseMap = new HashMap<String, String>();  
	private static final String yearReg="[一|二|三|四|五|六|七|八|九|十|〇|○]{4}年";  
	private static final String monthReg="(([十][一|二])|([一|二|三|四|五|六|七|八|九|十]))月";  
	private static final String dayReg="(([十][一|二|三|四|五|六|七|八|九])|(一|二|三|四|五|六|七|八|九|十)|([一|二|三][十][一|二|三|四|五|六|七|八|九]))日";  
	static{  
	    chineseMap.put("一", "1");  
	    chineseMap.put("元", "1");  
	    chineseMap.put("二", "2");  
	    chineseMap.put("三", "3");  
	    chineseMap.put("四", "4");  
	    chineseMap.put("五", "5");  
	    chineseMap.put("六", "6");  
	    chineseMap.put("七", "7");  
	    chineseMap.put("八", "8");  
	    chineseMap.put("九", "9");  
	    chineseMap.put("〇", "0");  
	    chineseMap.put("○", "0");  
	    chineseMap.put("十", "10");  
	    chineseMap.put("百", "100");  
	}  
	 protected static String regMethod(Pattern pattern, String value) {  
	    Matcher ma = pattern.matcher(value);  
	    if (ma.find()) {  
	        return ma.group();  
	    }  
	    return null;  
	}  
	  
	    private static int judgeChineseData(String value){  
	    int sumNum=0;  
	    int unitValue=0;  
	    for(int i=0;i<value.length()-1;i++){  
	        char te=value.charAt(i);  
	        int temp=Integer.parseInt(chineseMap.get(String.valueOf(te)));  
	        System.out.println(temp);
	        switch (temp) {  
	        case 100:  
	              if(unitValue==0){  
	                  unitValue=1;  
	              }  
	              sumNum+=unitValue*temp;  
	              unitValue=0;  
	            break;  
	        case 10:  
	             if(unitValue==0){  
	                  unitValue=1;  
	              }  
	              sumNum+=unitValue*temp;  
	              unitValue=0;  
	            break;  
	        default:  
	            unitValue+=temp;  
	            break;  
	        }  
	    }  
	    sumNum+= unitValue;  
	    return sumNum;  
	}  
	   
	    public static void main(String[] args) {
	    	String value = "一二三五年三月七日";
	    	//Pattern yearReg="[一|二|三|四|五|六|七|八|九|十|〇|○]{4}年"; 
	    	//regMethod(yearReg, value);
	    	System.out.println(judgeChineseData(value));
	    }

}
