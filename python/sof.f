C FILE: CALLBACK.F
      SUBROUTINE FOO(FUNC)
      EXTERNAL FUNC
      REAL*8 R
      R = 0D0
      R = R + FUNC(1)
      END
C END OF FILE CALLBACK.F
