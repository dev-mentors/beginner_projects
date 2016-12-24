using System;
using System.Collections.Generic;

namespace ConsoleApplication
{
    public class Deck
    {
        public List<Card> _cards { get; private set; }

        public Deck()
        {
            _cards = new List<Card>();
            Initialize();
        }

        public void Initialize()
        {
            for (var i = 1; i <= 13; i++)
            {
                _cards.Add(new Card(i, Suit.HEARTS));
                _cards.Add(new Card(i, Suit.SPADES));
                _cards.Add(new Card(i, Suit.DIAMONDS));
                _cards.Add(new Card(i, Suit.CLUBS));
            }
        }

        public void Shuffle()
        {
            Shuffle(_cards);
        }

        public void Shuffle<T>(IList<T> list)
        {
            int n = list.Count;
            Random rnd = new Random();
            while (n > 1)
            {
                int k = (rnd.Next(0, n) % n);
                n--;
                T value = list[k];
                list[k] = list[n];
                list[n] = value;
            }
        }
        public Card Deal(){
            var toReturn = _cards[0];
            _cards.RemoveAt(0);
            return toReturn;
        }

    }


}
