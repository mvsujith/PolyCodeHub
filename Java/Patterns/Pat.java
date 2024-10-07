package Java.Patterns;

public class Pat{
    public static void main(String[] args){
        pattern1(4);
        System.out.println();
        pattern2(4);
        System.out.println();
        patten3(4);
    }
    static void pattern1(int n){
        for(int row=1; row<=n; row++){
            for (int col = 1; col<=row; col++){
                System.out.print("*  ");
            }
            System.out.println();
        }
    }
    
    static void pattern2(int n){
        for(int row=1; row<=n; row++){
            for (int col=1; col<=n; col++){
                System.out.print("* ");

            }
            System.out.println();
        }
    }
    static void patten3(int n){
        for (int row = 1; row<=n; row++){
            for (int col = n; col<=n; col--){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
    static void patten3(int n){
        for (int row = 1; row<=n; row++){
            for (int col = n; col<=n; col--){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}