package blackjack; /**
 * Created by 1mike12 on 12/16/2016.
 */

import java.util.Scanner;

public class Blackjack {

    public static void main(String[] args) {

        System.out.println("Welcome to blackjack");

        Deck theDeck = new Deck();

        boolean continuePlaying = true;
        while (continuePlaying) {

            Hand myHand = new Hand();
            Hand dealerHand = new Hand();

            //run the program
            Card card = theDeck.drawCard();
            myHand.addCard(card);
            Card secondCard = theDeck.drawCard();
            myHand.addCard(secondCard);

            dealerHand.addCard(theDeck.drawCard());
            dealerHand.addCard(theDeck.drawCard());

            System.out.println(myHand.cards);
            System.out.println(myHand.getHandScore());

            System.out.println(dealerHand.cards);
            System.out.println(dealerHand.getHandScore());

            //display your hand value DONE

            System.out.println("Do you want to hit?");
            Scanner inputScanner = new Scanner(System.in);
            String answer = inputScanner.next();

            //ask if you want to hit?
            if (answer.equals("yes")) {
                myHand.addCard(theDeck.drawCard());
            } else {

            }

            System.out.println("Your hand : " + myHand.cards + ", score: " + myHand.getHandScore());
            System.out.println("Dealer's hand: " + dealerHand.cards + ", score: " + dealerHand.getHandScore());

            if (myHand.isBusted()) {
                System.out.println("you busted");
            } else {
                if (myHand.getHandScore() <= dealerHand.getHandScore()) {
                    System.out.println("you lose");
                } else {
                    System.out.println("you win");
                }
            }

            //continue playing?

            System.out.println("Continue playing?");
            String continuePlayingAnswer = inputScanner.next();

            //ask if you want to hit?
            if (!continuePlayingAnswer.equals("yes")) {
                continuePlaying = false;
            }
        }

        System.out.println("Thanks for playing!");
    }
}
