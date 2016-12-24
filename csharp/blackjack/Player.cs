using System;
using System.Collections.Generic;

namespace ConsoleApplication
{
    public class Player
    {
        public List<Card> Hand { get; set; }

        public Player()
        {
            Hand = new List<Card>();
        }

        public void Hit(Card c)
        {
            Hand.Add(c);
        }

        public int HandStrength()
        {
            int strength = 0;
            foreach (Card c in Hand)
            {
                strength += c._rank;
            }
            return strength;
        }
        public bool BustedCheck()
        {
            if (HandStrength() > 21)
            {
                return true;
            }
            return false;
        }
    }
}
