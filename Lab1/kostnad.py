def kostnad(p, r, a):
  """Beräknar den totala kostnaden för ett lån.

    Args:
        p (float): Lånebeloppet.
        r (float): Den årliga räntesatsen (i decimalform).
        a (float): Antal år för återbetalningen.

    Returns:
        Beräknar och skriver ut den totala kostnaden för ett lån.
  """
  total_kostnad = p + (a + 1) * p * r / 2.0

  print(f"Den totala kostnaden efter {a} år är : {total_kostnad:.2f} kr")