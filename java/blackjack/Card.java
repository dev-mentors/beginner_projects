package blackjack;

/**
 * Created by 1mike12 on 12/16/2016.
 */
public class Card {

    static String description = "Glossy paper card with blue backing";

    String suite;
    int rank;

    Card(String suite, int rank) {
        this.suite = suite;
        this.rank = rank;
    }

    public String toString() {
        return this.suite + String.valueOf(this.rank);
    }

    int getScore() {

        if (rank == 1) {
            return 11;
        } else if (rank >= 10) {
            return 10;
        } else {
            return rank;
        }
    }
}
