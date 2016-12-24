package blackjack;

import java.util.ArrayList;

/**
 * Created by 1mike12 on 12/16/2016.
 */
public class Hand {

    ArrayList<Card> cards = new ArrayList<>();

    Hand() {

    }

    void addCard(Card card) {
        cards.add(card);
    }

    int getHandScore() {
        int score = 0;

        for (Card card : cards) {
            score = score + card.getScore();
        }
        return score;
    }

    boolean isBusted() {
        return getHandScore() > 21;
    }
}
