int led11 = 32;
int led12 = 25;
int led13 = 26;

int led21 = 0;
int led22 = 16;
int led23 = 17;

int led31 = 5;
int led32 = 18;
int led33 = 19;

int led41 = 21;
int led42 = 22;
int led43 = 23;

int buzzer = 14;

int currentrow;
int currentcolumn = 0;

int btnChange = 15;
bool btnPrevState = 0;
bool btsState = 0;

int diff = 1;

int start = 0;

int btnRow = 2;
int btnRowPrev = 0;
int btnRowState = 0;

int rij1[] = {led11, led12, led13};
int rij2[] = {led21, led22, led23};
int rij3[] = {led31, led32, led33};
int rij4[] = {led41, led42, led43};

int aangeduide_rijen[] = {1, 1, 1};

int rijen[4][3] = {
    {led11, led12, led13},
    {led21, led22, led23},
    {led31, led32, led33},
    {led41, led42, led43}};

int score = 0;
int chosen = 10;
int number;
int tussentijd = 25;
int moeilijkheidsgraad = 1;

int waardePot = 0;
int prevPot = 0;
// Potentiometer is connected to GPIO 34 (Analog ADC1_CH6)
int potPin = 13;
int v = 0;
int attem = 0;

void setup()
{
    Serial.begin(9600);
    // put your setup code here, to run once:
    pinMode(led11, OUTPUT);
    pinMode(led12, OUTPUT);
    pinMode(led13, OUTPUT);

    pinMode(led21, OUTPUT);
    pinMode(led22, OUTPUT);
    pinMode(led23, OUTPUT);

    pinMode(led31, OUTPUT);
    pinMode(led32, OUTPUT);
    pinMode(led33, OUTPUT);

    pinMode(buzzer, OUTPUT);

    pinMode(led41, OUTPUT);
    pinMode(led42, OUTPUT);
    pinMode(led43, OUTPUT);
    pinMode(potPin, INPUT);
    pinMode(btnChange, INPUT_PULLUP);
    pinMode(btnRow, INPUT_PULLUP);
    randomSeed(digitalRead(A5));
    number = random(0, 3);
}

void rijAanUit(int row)
{
    // int rij [3] = {led11,led12,led13};
    // currentrow = row;
    // if (row ==2){
    // int rij [3]= {led21,led22,led23};
    // }
    // else if(row==3){
    // int rij [3]= {led31,led32,led33};
    // }
    // else if(row==4){
    // int rij [3]= {led41,led42,led43};
    // }
    int c = 0;
    delay(20);
    for (int i = 0; i < 3; i++)
    {
        if (aangeduide_rijen[i] == 1)
        {
            digitalWrite(rijen[row][i], HIGH);
            btsState = digitalRead(btnChange);
            changeRow();
            if (btsState != btnPrevState)
            {
                all_out();
                attem += 1;
                digitalWrite(rijen[row][currentcolumn], HIGH);
                delay(1000);
                digitalWrite(rijen[row][currentcolumn], LOW);
                if (row + 1 == chosen)
                {
                    aangeduide_rijen[currentcolumn] = 0;
                    if (aangeduide_rijen[0] == 0)
                    {
                        if (aangeduide_rijen[1] == 0)
                        {
                            if (aangeduide_rijen[2] == 0)
                            {
                            }
                            else
                            {
                                digitalWrite(rij1[currentcolumn], LOW);
                                currentcolumn = 2;
                                digitalWrite(rij1[currentcolumn], HIGH);
                            }
                        }
                        else
                        {
                            digitalWrite(rij1[currentcolumn], LOW);
                            currentcolumn = 1;
                            digitalWrite(rij1[currentcolumn], HIGH);
                        }
                    }
                    else
                    {
                        digitalWrite(rij1[currentcolumn], LOW);
                        currentcolumn = 0;
                        digitalWrite(rij1[currentcolumn], HIGH);
                    }
                    score += 1;
                    buzz(200);
                    Serial.println("score " + String(score));
                    if (diff != 3 && tussentijd >= 10)
                    {
                        tussentijd = tussentijd - 10;
                    }
                }
                else
                {
                    buzz(800);
                    all_on();
                    delay(100);
                    all_out();
                    delay(100);
                    all_on();
                    delay(100);
                    all_out();
                    delay(100);
                }
            }
        }
    }

    delay(100);

    for (int i = 0; i < 3; i++)
    { // for each element in the array
        digitalWrite(rijen[row][i], LOW);
        btsState = digitalRead(btnChange);
        changeRow();
        if (btsState != btnPrevState)
        {
            attem += 1;
            all_out();
            digitalWrite(rijen[row][currentcolumn], HIGH);
            delay(1000);
            digitalWrite(rijen[row][currentcolumn], LOW);
            if (row + 1 == chosen)
            {
                buzz(200);
                score += 1;
                aangeduide_rijen[currentcolumn] = 0;
                if (aangeduide_rijen[0] == 0)
                {
                    if (aangeduide_rijen[1] == 0)
                    {
                        if (aangeduide_rijen[2] == 0)
                        {
                        }
                        else
                        {
                            digitalWrite(rij1[currentcolumn], LOW);
                            currentcolumn = 2;
                            digitalWrite(rij1[currentcolumn], HIGH);
                        }
                    }
                    else
                    {
                        digitalWrite(rij1[currentcolumn], LOW);
                        currentcolumn = 1;
                        digitalWrite(rij1[currentcolumn], HIGH);
                    }
                }
                else
                {
                    digitalWrite(rij1[currentcolumn], LOW);
                    currentcolumn = 0;
                    digitalWrite(rij1[currentcolumn], HIGH);
                }
                Serial.println("score " + String(score));
                if (diff != 3 && tussentijd >= 10)
                {
                    tussentijd = tussentijd - 10;
                }
            }
            else
            {
                buzz(800);
                all_on();
                delay(100);
                all_out();
                delay(100);
                all_on();
                delay(100);
                all_out();
                delay(100);
            }
        }
    }

    // delay(20);
    // for (int element : rij) { // for each element in the array
    // Serial.println(element);

    // btsState =digitalRead(btnChange);
    // if(btsState != btnPrevState){
    // delay(2000);
    // if (row == chosen){
    // score +=1;
    // Serial.println("score"+ String(score));
    // }
    // }
    // }
}

void changeRow()
{
    btnRowState = digitalRead(btnRow);

    if (btnRowState != btnRowPrev)
    {
        // Serial.println(btnRowState);
        // Serial.println(btnRowPrev);
        if (currentcolumn == 0)
        {
            delay(10);
            if (aangeduide_rijen[1] == 1)
            {
                currentcolumn = 1;
                digitalWrite(led11, LOW);
                digitalWrite(led12, HIGH);
                delay(300);
                return;
            }
            else
            {
                if (aangeduide_rijen[2] == 1)
                {
                    currentcolumn = 2;
                    digitalWrite(led11, LOW);
                    digitalWrite(led13, HIGH);
                    delay(300);
                    return;
                }
                else
                {
                    delay(300);
                    return;
                }
            }
        }

        if (currentcolumn == 1)
        {
            delay(10);
            if (aangeduide_rijen[2] == 1)
            {
                currentcolumn = 2;
                digitalWrite(led12, LOW);
                digitalWrite(led13, HIGH);
                delay(300);
                return;
            }
            else
            {
                if (aangeduide_rijen[0] == 1)
                {
                    currentcolumn = 0;
                    digitalWrite(led12, LOW);
                    digitalWrite(led11, HIGH);
                    delay(300);
                    return;
                }
                else
                {
                    delay(300);
                    return;
                }
            }
        }

        if (currentcolumn == 2)
        {
            delay(10);
            if (aangeduide_rijen[0] == 1)
            {
                currentcolumn = 0;
                digitalWrite(led13, LOW);
                digitalWrite(led11, HIGH);
                delay(300);
                return;
            }
            else
            {
                if (aangeduide_rijen[1] == 1)
                {
                    currentcolumn = 1;
                    digitalWrite(led13, LOW);
                    digitalWrite(led12, HIGH);
                    delay(300);
                    return;
                }
                else
                {
                    delay(300);
                    return;
                }
            }
        }
    }
}

void all_out()
{
    digitalWrite(led21, LOW);
    digitalWrite(led22, LOW);
    digitalWrite(led23, LOW);

    digitalWrite(led31, LOW);
    digitalWrite(led32, LOW);
    digitalWrite(led33, LOW);

    digitalWrite(led41, LOW);
    digitalWrite(led42, LOW);
    digitalWrite(led43, LOW);
    delay(10);
}

void all_on()
{
    digitalWrite(led21, HIGH);
    digitalWrite(led22, HIGH);
    digitalWrite(led23, HIGH);

    digitalWrite(led31, HIGH);
    digitalWrite(led32, HIGH);
    digitalWrite(led33, HIGH);

    digitalWrite(led41, HIGH);
    digitalWrite(led42, HIGH);
    digitalWrite(led43, HIGH);
    delay(10);
}

void buzz(int buzzdelay)
{
    for (int i = 0; i < 500; i++)
    {
        digitalWrite(buzzer, 1);
        delayMicroseconds(buzzdelay);
        digitalWrite(buzzer, 0);
        delayMicroseconds(buzzdelay);
    }
    return;
}

void level(int nr)
{
    if (nr == 1)
    {
        digitalWrite(led11, HIGH);
        return;
    }

    if (nr == 2)
    {
        digitalWrite(led11, 1);
        digitalWrite(led12, 1);
        return;
    }
    if (nr == 3)
    {
        digitalWrite(led11, 1);
        digitalWrite(led12, 1);
        digitalWrite(led13, 1);
        return;
    }
}

void levelout()
{
    digitalWrite(led11, 0);
    digitalWrite(led12, 0);
    digitalWrite(led13, 0);
}

void (*resetFunc)(void) = 0;
// delay(tussentijd);
// btsState =digitalRead(btnChange);
// for (int element : rij3) { // for each element in the array
// digitalWrite(element,LOW);
// }

// }

void loop()
{
    if (score == 4)
    {
        btsState = digitalRead(btnChange);
        start = 2;
        if (btsState != btnPrevState)
        {
            resetFunc();
        }
    }
    if (score == 3)
    {
        digitalWrite(led11, LOW);
        digitalWrite(led12, LOW);
        digitalWrite(led13, LOW);

        Serial.println("Game Gedaan");
        Serial.println("In " + String(attem) + " attempts. Op diff: " + String(diff));
        score += 1;
    }
    if (start == 0)
    {
        all_out();
        if (v == 0)
        {
            Serial.println("Kies GameMode");
            Serial.println("Als je gekozen hebt mag je op de knop drukken");
            diff = 1;
            Serial.println("De gekozen difficulity is:" + String(diff));
            level(diff);
            v += 1;
        }
        waardePot = round(analogRead(potPin) / 1365);
        if (waardePot != prevPot && waardePot != 0)
        {
            Serial.println("Kies GameMode");
            Serial.println("Als je gekozen hebt mag je op de knop drukken");
            Serial.println("De gekozen difficulity is:" + String(waardePot));
            prevPot = waardePot;
            diff = waardePot;
            levelout();
            level(diff);
            delay(300);
        }
        btsState = digitalRead(btnChange);
        if (btsState != btnPrevState)
        {
            start = 1;
            levelout();
        }
    }
    if (start == 1)
    {

        // put your main code here, to run repeatedly:
        if (chosen == 10)
        {
            btsState = digitalRead(btnChange);
            btnRowState = digitalRead(btnRow);
            currentcolumn = 0;
            digitalWrite(led11, HIGH);
            if (number == 0)
            {
                for (int element : rij2)
                { // for each element in the array
                    digitalWrite(element, HIGH);
                    chosen = 2;
                }
                delay(2000);
                for (int element : rij2)
                { // for each element in the array
                    digitalWrite(element, LOW);
                }
            }
            else if (number == 1)
            {
                for (int element : rij3)
                { // for each element in the array
                    digitalWrite(element, HIGH);
                    chosen = 3;
                }
                delay(2000);
                for (int element : rij3)
                { // for each element in the array
                    digitalWrite(element, LOW);
                }
            }
            else if (number == 2)
            {
                for (int element : rij4)
                { // for each element in the array
                    digitalWrite(element, HIGH);
                    chosen = 4;
                }
                delay(2000);
                for (int element : rij4)
                { // for each element in the array
                    digitalWrite(element, LOW);
                }
            }
        }
        // Hier begint het spelletje zelf

        if (diff == 1)
        {

            // Rij 1
            rijAanUit(1);
            delay(tussentijd);

            // rij2
            rijAanUit(2);
            delay(tussentijd);

            // rij3
            rijAanUit(3);
            delay(tussentijd);

            delay(tussentijd / 2);
            btsState = digitalRead(btnChange);
            btnRowState = digitalRead(btnRow);
        }

        if (diff == 2)
        {
            if (score == 0)
            {

                // Rij 1
                rijAanUit(1);
                delay(tussentijd);

                // rij2
                rijAanUit(2);
                delay(tussentijd);

                // rij3
                rijAanUit(3);
                delay(tussentijd);

                delay(tussentijd / 2);
                btsState = digitalRead(btnChange);
            }
            if (score == 1)
            {

                // Rij 1
                rijAanUit(3);
                delay(tussentijd);

                // rij2
                rijAanUit(2);
                delay(tussentijd);

                // rij3
                rijAanUit(1);
                delay(tussentijd);

                delay(tussentijd / 2);
                btsState = digitalRead(btnChange);
            }

            if (score == 2)
            {
                // Rij 1
                rijAanUit(1);
                delay(tussentijd);

                // rij2
                rijAanUit(2);
                delay(tussentijd);

                // rij3
                rijAanUit(3);
                delay(tussentijd);

                delay(tussentijd / 2);
                btsState = digitalRead(btnChange);
            }
        }
        if (diff == 3)
        {
            if (score == 0)
            {
                tussentijd = random(15, 20);
                // Rij 1
                rijAanUit(1);
                delay(tussentijd);

                // rij2
                rijAanUit(2);
                delay(tussentijd);

                // rij3
                rijAanUit(3);
                delay(tussentijd);

                delay(tussentijd / 2);
                btsState = digitalRead(btnChange);
            }
            if (score == 1)
            {
                tussentijd = random(8, 14);
                // Rij 1
                rijAanUit(3);
                delay(tussentijd);

                // rij2
                rijAanUit(2);
                delay(tussentijd);

                // rij3
                rijAanUit(1);
                delay(tussentijd);

                delay(tussentijd / 2);
                btsState = digitalRead(btnChange);
            }

            if (score == 2)
            {
                tussentijd = random(3, 7);
                // Rij 1
                rijAanUit(1);
                delay(tussentijd);

                // rij2
                rijAanUit(2);
                delay(tussentijd);

                // rij3
                rijAanUit(3);
                delay(tussentijd);

                delay(tussentijd / 2);
                btsState = digitalRead(btnChange);
            }
        }
    }
}