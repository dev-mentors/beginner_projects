package blackjack;

import java.util.ArrayList;
import java.util.Collections;

/**
 * Created by 1mike12 on 12/16/2016.
 */
public class Deck {

    ArrayList<Card> cards = new ArrayList();

    Deck() {

        for (int i = 1; i < 14; i++) {
            Card newCard = new Card("H", i);
            cards.add(newCard);
        }

        for (int i = 1; i < 14; i++) {
            Card newCard = new Card("S", i);
            cards.add(newCard);
        }

        for (int i = 1; i < 14; i++) {
            Card newCard = new Card("D", i);
            cards.add(newCard);
        }

        for (int i = 1; i < 14; i++) {
            Card newCard = new Card("C", i);
            cards.add(newCard);
        }

        Collections.shuffle(cards);
    }

    Card drawCard() {
        Card theRemovedCard = cards.remove(0);
        return theRemovedCard;
    }
}
