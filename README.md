# Hero_game
Hero_game is game that asks some question in math and decoding to kill enemy and be the hero of the village





import java.util.Random;
import java.util.Scanner;
import java.util.ArrayList;


//import java.util.Random;
//import java.util.Scanner;
//import java.util.ArrayList;



public class final_version_Naca_game
{
    ///static int k = 0;
   /// static String[] my_bag;
   	static ArrayList <String> weopens = new ArrayList <String> ();
	static Scanner sc =new Scanner(System.in);
	static int player_life = 0;
    static int sec = 100;
    static int  ans_weop_checker = 0 ;
    static int ans_win_checker = 0;
    static String[] weopens_list = {"Sowrd","Thor Hammer","Benten Watch","Zanos Glove"};
    static String[] enemies = {"Pirates " ,"Thieves ","Aliens ","Troll "};
    static String weopen = random(weopens_list);
	static String enemy = random(enemies);
	
	public static String random(String[] array) {
	    
		   Random rand = new Random();
		   int randomIndex = rand.nextInt(array.length);
		   String randomElement = array[randomIndex];
		   return randomElement;
	}
	
	
	

		
	public static void printT(String mesg) {
	    
		try {
			Thread.sleep(sec);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println(mesg);
		
	}
	
	public static void printT(String[] mesg) {
	
		for (String i : mesg) {
			
			try {
				Thread.sleep(sec);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			
			System.out.println(i);
		}
	}
	
	
	
	public static void main(String[] args) {   //////////////////////////////////// 00000  main method   000000000000  /////////////////
	        
	        user_name();

	}
	
	
	
	
	public static void user_name(){
	    
	    printT("Enter your name here please : ");
	    String name = sc.next();
	    printT("Hello Mr/Ms "+ name + " in our game......");
	    
	    opning_fun();
	    
	}
	
	
	public static void answer_checker(){
	    

	    if(ans_weop_checker != 0){
	        
	        printT("Emmbressive the answer is ***correct*** ");
	        String[] get_weop = {"You discard your silly old dagger and take the "+weopen+" with you.",
                                 "You walk back out to the field."};
	        printT(get_weop);
	        weopens.add(weopen);
            cave_q1();
	        
	    }
	    else
	    {

	        printT("you can not get the weapon and the man kick you out of the cave ---");
	        first_quest();
	       
	    }
	    
	}
	
	
	public static void Quetions_weop(){
	    
	    String[] quetions = {"    What is the integration of Zero ?",
	                         "    what is the defferintial of x ?"};
	    String quetion_weop = random(quetions);
	    printT(quetion_weop);
	    printT("     Please Write in smallcase letters : ");
	    
	    String ans = sc.next();
	    
	    if(quetion_weop.equals("    What is the integration of Zero ?")){
	        
	        if(ans.equals("const")|| ans.equals("constant"))
	        {
	            
	            ans_weop_checker = 1;
	            answer_checker();
	        }
	        else
	        {
	            answer_checker();
	        }
	        
	    }
	    else if(quetion_weop.equals("    what is the defferintial of x ?")){
	        
	        if(ans.equals("1")|| ans.equals("one"))
	        {
	            ans_weop_checker = 1;
	            answer_checker();
	        }
	        else{
	            
	            answer_checker();
	        
	            
	        }
	        
	        
	    }
	    else{
	        Quetions_weop();
	    }
	    
	    
	}
	

	
	
	public static void win_checker(){
	    
	    
	   
	    if(ans_win_checker != 0){
	        
	        printT("Emmbressive the answer is ********* correct ********* ");
	       String[] cav1 = {"As the " + enemy + " moves to attack, you unsheath your new "+weopen+".",
                            "The "+ weopen +"  shines brightly in your hand as you brace yourself for the attack.",
                            "But the " + enemy +" takes one look at your shiny new "+weopen+" and runs away!",
                            "You have rid the town of the " + enemy + " .",
                            "You are *************** victorious *************** ",
                            "*************************************************"};
            printT(cav1);
            replay_game();
	        

	    }
	    else
	    {
	        
	        if(player_life != 0){
	            
	            printT("the answer is Wrong for second time "+enemy+"attack you with a deadly attack");
	            printT("your life percent becomes *| 0% |*");
                printT("!!!!!!!!!!! you die !!!!!!!!!!!");
                replay_game();
	        }
	        else{
	            

	            String[] last_chance = {"Wrong answer . "+ enemy +" attacks They attack you ",
	                                    " that attack affected half of your life. You have a chance",
	                                    "your live now decreased to half your live percent becomes **| 50% |**",
	                                    "to make anthor attack before you die Try your best in your attack...",};
	            printT(last_chance);
	            player_life += 1;
	            Quetions_win();

	       }
	        

	   }
	    
	}
	
	
	
	
		public static void Quetions_win(){
	    
	    printT("you in front of "+enemy+" and you attack them to kill there ***Boss***");
	    
	    String[] quetions = {"        What is the limit of e^x when x go to negative Infinity?",
	                         "        what is decode 01001110 01000001 01000011 01000001 01010100 01000101 01000001 01001101 to  ASCII?"};
	    String quetion_win = random(quetions);
	    printT(quetion_win);
	    printT("         Write answer here :");
	    
	    String ans = sc.next();
	   
	    
	    if(quetion_win.equals("        What is the limit of e^x when x go to negative Infinity?")){
	        
	        if(ans.equals("zero")|| ans.equals("0"))
	        {
	            
	            ans_win_checker = 1;
	            win_checker();
	        }
	        else
	        {
	            win_checker();
	        }
	        
	    }
	    else if(quetion_win.equals("        what is decode 01001110 01000001 01010011 01000001 01010100 01000101 01000001 01001101 to  ASCII?")){
	        
	        if(ans.equals("NASATEAM"))
	        {
	            ans_weop_checker = 1;
	            win_checker();
	        }
	        else{
	            
	            win_checker();
	        
	            
	        }
	        
	        
	    }
	    else{
	        Quetions_win();
	    }
	    
	    
	}
	
	
	
	
	
	
	public static void opning_fun(){
	    
	    printT("your life percent now is ***| 100% |***");
	    
	    String[] opning_statment={"You find yourself standing in an open field, filled with grass and yellow wildflowers.",
                                  "Rumor has it that a Aliens  is somewhere around here, and has been terrifying the nearby village.",
                                  "In front of you is a house.",
                                  "To your right is a dark cave.",
                                  "In your hand you hold your trusty (but not very effective) dagger."};
                         
        printT(opning_statment);
        first_quest();


	}
	
	
	
	public static void first_quest() {
        
		   String choice;

	       String[] fir_q  =  {"      Enter 1 to knock on the door of the house.",
			                   "      Enter 2 to peer into the cave.",
		                 	   "      What would you like to do?",
                               "      (Please enter 1 or 2.)"};
            
            printT(fir_q);
            
            choice =sc.next();
             
			String cho = "one";

            
            if (choice.equals("1") || choice.equals("one") ) 
            {
            	house();
            }
            else if ( choice.equals("2") || choice.equals("two") ) 
            {
            	cave();
            }
            else
            {
            	first_quest();
            }
           
                
	}
	
	
	
    public static void house(){
    

	   String[] house_text = {"you approach the door of the house", 
	                          "you are about to knock when the door opens.and out steps a " + enemy +" .",
                              "Eep! this is the  " +enemy +" house !",
	                          "the " + enemy + " attacks you! ",
                              "you feel a bit under prepared for this , what with only having a tiny dagger."};
                                  
            printT(house_text);
            house_q1();

    }	
	
	
	
	
	
	public static void house_q1() {

		printT("Would you like to (1) fight or (2) run away?");

		String ch1 = sc.next();
		String[] ans = {"You do your best...",
						"but your dagger is no match for the "+ enemy + ".",
						"You have been defeated!",
						"your life percent *| 0% |* ",
						"you !!!!!!! die !!!!!!!"};
		///ans[1] = ans[1] + " " + enemy;

		if (ch1.equals("1") || ch1.equals("one")) {
			
			printT(ans);
			replay_game();
			
		 }
		 else if(ch1.equals("2") || ch1.equals("two"))
		 {
		        printT("You run back into the field. Luckily, you don't seem to have been followed.");
		        first_quest();
		 }
		 else
		 {
		     house_q1();
		 }
		
	}
	
	public static void cave(){
	    
	    if (weopens.contains(weopen)){
	        
	       String[] again={"You peer cautiously into the cave.",
                           "You've been here before, and gotten all the good stuff. It's just an empty cave now.",
                           "You walk back out to the field."};
           printT(again);
           cave_q1();
	    }
	    else{
	        
	        String[] mass_c= {"You peer cautiously into the cave.",
                            "It turns out to be only a very small cave.",
                            "Your eye catches a light behind a rock.",
                            "You have found the magical "+ weopen +" !",
                            "And there is a wised man in the cave say"+ 
                            " ('that if you want take the "+ weopen +" you shoud answer this Quetion')"};
            printT(mass_c);
            Quetions_weop();
            
            //    k = 1;
           // my_bag[0] = "sword";
           // printT(my_bag);

	    }
	    
	    
	    
	    
	}
	
	
	public static void cave_q1(){
	    
        
        
            
	   String[] q2= {"    Enter 1 to knock on the door of the house. And attack "+ enemy +" ",
                    "    Enter 2 to peer into the cave.",
                    "    What would you like to do?",
                    "    (Please enter 1 or 2 ) :"};
            printT(q2);
        
            String ans2 = sc.next();
            
        
        
        
        if (ans2.equals("1") || ans2.equals("one") ){
            
            Quetions_win();
            

           // replay_game();
        
        
        }
         else if (ans2.equals("2") || ans2.equals("two")){

              cave();
         }
        else{

             cave_q1();
        } 
        
        
	}
	


	public static void 	replay_game() {
		
		printT("if you want to play my game again please enter (yes/ no): ");
		
		String ans = sc.next();
		
		if(ans.equals("yes") || ans.equals("YES")){
		    player_life = 0;
		    weopens.clear();
		    opning_fun();
		}
		else if (ans.equals("no") || ans.equals("NO")){
		    
		    printT("............... Good bye ...............");
		    
		    //System.exit(0);
		    
		} 
		else
		{
		    
		    replay_game();
		}
		
	}


	
	
}
