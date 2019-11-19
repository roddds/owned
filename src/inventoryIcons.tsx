import React from 'react';
import { ReactComponent as Item1 } from './items/1-amulet.svg';
import { ReactComponent as Item2 } from './items/2-master-key.svg';
import { ReactComponent as Item3 } from './items/3-laila-hd-copy.svg';
import { ReactComponent as Item4 } from './items/4-email.svg';
import { ReactComponent as Item5 } from './items/5-ipod.svg';
import { ReactComponent as Item6 } from './items/6-coin-purse.svg';
import { ReactComponent as Item7 } from './items/7-100-bill.svg';
import { ReactComponent as Item8 } from './items/8-tupperware.svg';
import { ReactComponent as Item9 } from './items/9-brochure.svg';
import { ReactComponent as Item10 } from './items/10-coin-purse-full.svg';
import { ReactComponent as Item11 } from './items/11-console-vintage.svg';
import { ReactComponent as Item12 } from './items/12-coxinha.svg';
import { ReactComponent as Item13 } from './items/13-edgar-hd.svg';
import { ReactComponent as Item14 } from './items/14-loss.svg';
import { ReactComponent as Item15 } from './items/15-smg.svg';
import { ReactComponent as Item16 } from './items/16-ammo.svg';
import { ReactComponent as Item17 } from './items/17-pistol.svg';
import { ReactComponent as Item18 } from './items/18-charm.svg';
import { ReactComponent as Item19 } from './items/19-suitcase.svg';
import { ReactComponent as Item20 } from './items/20-exit-key.svg';
import { ReactComponent as Item21 } from './items/21-screwdriver.svg';
import { ReactComponent as Item22 } from './items/22-broom.svg';
import { ReactComponent as Item23 } from './items/23-regular-key.svg';
import { ReactComponent as Item24 } from './items/24-rifle.svg';
import { ReactComponent as Item25 } from './items/25-grenade.svg';
import { ReactComponent as Item26 } from './items/26-backpack.svg';
import { ReactComponent as Item27 } from './items/27-first-aid-kit.svg';
import { ReactComponent as Item28 } from './items/28-sunglasses.svg';

interface Icons {
  [key: string]: React.FunctionComponent<React.SVGProps<SVGSVGElement>>;
}

const icons: Icons = {
  '1-amulet.svg': Item1,
  '2-master-key.svg': Item2,
  '3-laila-hd-copy.svg': Item3,
  '4-email.svg': Item4,
  '5-ipod.svg': Item5,
  '6-coin-purse.svg': Item6,
  '7-100-bill.svg': Item7,
  '8-tupperware.svg': Item8,
  '9-brochure.svg': Item9,
  '10-coin-purse-full.svg': Item10,
  '11-console-vintage.svg': Item11,
  '12-coxinha.svg': Item12,
  '13-edgar-hd.svg': Item13,
  '14-loss.svg': Item14,
  '15-smg.svg': Item15,
  '16-ammo.svg': Item16,
  '17-pistol.svg': Item17,
  '18-charm.svg': Item18,
  '19-suitcase.svg': Item19,
  '20-exit-key.svg': Item20,
  '21-screwdriver.svg': Item21,
  '22-broom.svg': Item22,
  '23-regular-key.svg': Item23,
  '24-rifle.svg': Item24,
  '25-grenade.svg': Item25,
  '26-backpack.svg': Item26,
  '27-first-aid-kit.svg': Item27,
  '28-sunglasses.svg': Item28
};

export default icons;
