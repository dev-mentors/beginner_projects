using System;

namespace ConsoleApplication
{
    public class Blackjack
    {
        public Deck _theDeck { get; set; }
        public Player _player1 { get; set; }
        public Player _player2 { get; set; }

        public Blackjack()
        {
            _theDeck = new Deck();
            _theDeck.Shuffle();

            _player1 = new Player();
            _player2 = new Player();
        }

        public void Play()
        {
            _player1.Hit(_theDeck.Deal());
            _player1.Hit(_theDeck.Deal());



            Console.WriteLine(_player1.HandStrength());

            while (_player1.HandStrength() < 21)
            {
                Console.WriteLine("would you like to 'hit'?");
                var res = Console.ReadLine();
                if (res == "hit")
                {
                    _player1.Hit(_theDeck.Deal());
                    System.Console.WriteLine(_player1.HandStrength());
                }
                else
                {
                    break;
                }
            }

            var hasBusted = _player1.BustedCheck();
            if (hasBusted)
            {
                System.Console.WriteLine("you lose");
                return;
            }

            _player2.Hit(_theDeck.Deal());
            _player2.Hit(_theDeck.Deal());

            while (_player2.HandStrength() < 17)
            {
                _player2.Hit(_theDeck.Deal());
            }
            if (_player2.BustedCheck())
            {
                System.Console.WriteLine("Dealer's busted, you win!");
                return;
            }

            var dealerStrength = _player2.HandStrength();
            var playerStrength = _player1.HandStrength();

            if (dealerStrength == playerStrength)
            {
                System.Console.WriteLine($"Pushed. Dealer has: {dealerStrength}, player has: {playerStrength}");
            }
            else if (dealerStrength > playerStrength)
            {
                System.Console.WriteLine($"Dealer won. Dealer has: {dealerStrength}, player has: {playerStrength}");
            }
            else
            {
                System.Console.WriteLine($"Player won. Dealer has: {dealerStrength}, player has: {playerStrength}");
            }

        }

    }
}
