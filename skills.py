from abc import ABC, abstractmethod


class Skill(ABC):
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self):
        pass

    def _is_stamina_enough(self):
        return self.user.stamina > self.stamina

    def use(self, user, target) -> str:
        self.user = user
        self.target = target
        if self._is_stamina_enough():
            return self.skill_effect()
        return f"{self.user.name} хотел использовать {self.name}, но у него не хватило выносливости."


class FurryPunch(Skill):
    name = 'Свирепый пинок'
    stamina = 6
    damage = 12

    def skill_effect(self):
       self.user.stamina -= self.stamina
       self.target.get_damage(self.damage)
       return f"{self.user.name} использует {self.name} и наносит {self.damage} урона противнику"


class HardShot(Skill):
    name = "Мощный укол"
    stamina = 5
    damage = 15

    def skill_effect(self):
       self.user.stamina -= self.stamina
       self.target.get_damage(self.damage)
       return f"{self.user.name} использует {self.name} и наносит {self.damage} урона противнику"