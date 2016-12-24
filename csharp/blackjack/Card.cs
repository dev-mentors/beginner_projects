using System;

namespace ConsoleApplication
{
    public class Card
    {
        public int _rank { get; set; }
        public Suit _suit { get; set; }
        public Card(int r, Suit s)
        {
            _rank = r;
            _suit = s;
        }
    }
    public enum Suit
    {
        HEARTS,
        SPADES,
        DIAMONDS,
        CLUBS
    }
}
