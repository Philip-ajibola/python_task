import unittest

from gun.gun import Gun
from gun.type import Type
from gun.safety_exception import SafetyException


class MyTestCase(unittest.TestCase):
    def test_gun_can_be_created(self):
        new_gun = Gun(Type.PISTOL, 10)
        self.assertEqual(10, new_gun.number_of_bullets())

    def test_gun_cant_be_given_negative_bullets(self):
        with self.assertRaises(ValueError): new_gun = Gun(Type.PISTOL, -10)

    def test_pistol_cant_take_more_than_10_bullets(self):
        with self.assertRaises(ValueError): new_gun = Gun(Type.PISTOL, 15)

    def test_shotgun_cant_take_more_than_two_bullets(self):
        with self.assertRaises(ValueError): new_gun = Gun(Type.SHOTGUN, 3)

    def test_rifle_cant_take_more_than_25_bullets(self):
        with self.assertRaises(ValueError): new_gun = Gun(Type.RIFLE, 30)

    def test_revolver_cant_take_more_than_150_bullets(self):
        with self.assertRaises(ValueError): new_gun = Gun(Type.RIFLE, 200)

    def test_gun_can_be_shot(self):
        new_gun = Gun(Type.PISTOL, 10)
        self.assertTrue(new_gun.safety_check())

        new_gun.toggle_safety()
        new_gun.shoot()
        self.assertEqual(9, new_gun.number_of_bullets())

        for i in range(5):
            new_gun.shoot()
        self.assertEqual(4, new_gun.number_of_bullets())

    def test_gun_cant_shoot_if_bullet_finish(self):
        new_gun = Gun(Type.PISTOL, 10)
        self.assertEqual(10, new_gun.number_of_bullets())

        new_gun.toggle_safety()
        for i in range(10):
            new_gun.shoot()
        self.assertEqual(0, new_gun.number_of_bullets())

        with self.assertRaises(ValueError): new_gun.shoot()

    def test_gun_can_be_reloaded(self):
        new_gun = Gun(Type.PISTOL, 10)
        self.assertEqual(10, new_gun.number_of_bullets())

        new_gun.toggle_safety()
        for i in range(10):
            new_gun.shoot()
        self.assertEqual(0, new_gun.number_of_bullets())

        new_gun.reload()
        self.assertEqual(10, new_gun.number_of_bullets())

        for i in range(5):
            new_gun.shoot()
        self.assertEqual(5, new_gun.number_of_bullets())

        new_gun.reload()
        self.assertEqual(10, new_gun.number_of_bullets())

    def test_gun_cant_shoot_if_safety_on(self):
        new_gun = Gun(Type.PISTOL, 10)
        self.assertTrue(new_gun.safety_check())

        with self.assertRaises(SafetyException): new_gun.shoot()