//
//  ViewController.swift
//  Musical Ear
//
//  Created by Nicolas Guardado Guardado on 8/25/23.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var rootLabel: UILabel! // 1
    @IBOutlet weak var minorSecondLabel: UILabel! // 2
    @IBOutlet weak var majorSecondLabel: UILabel! // 3
    @IBOutlet weak var minorThirdLabel: UILabel! // 4
    @IBOutlet weak var majorThirdLabel: UILabel! // 5
    @IBOutlet weak var perfectFourthLabel: UILabel! // 6
    @IBOutlet weak var tritoneLabel: UILabel! // 7
    @IBOutlet weak var perfectFifthLabel: UILabel! // 8
    @IBOutlet weak var minorSixthLabel: UILabel! // 9
    @IBOutlet weak var majorSixthLabel: UILabel! // 10
    @IBOutlet weak var minorSeventhLabel: UILabel! // 11
    @IBOutlet weak var majorSeventhLabel: UILabel! // 12
    @IBOutlet weak var octaveLabel: UILabel! // 13
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func createInterval(_ sender: Any) {
        
        // 1
        if (true) { // Root is always true
            rootLabel.text = "Root"
        }
        // 2
        if (Bool.random()) {
            minorSecondLabel.text = "Minor Second"
        } else {
            minorSecondLabel.text = ""
        }
        // 3
        if (Bool.random()) {
            majorSecondLabel.text = "Major Second"
        } else {
            majorSecondLabel.text = ""
        }
        // 4
        if (Bool.random()) {
            minorThirdLabel.text = "Minor Third"
        } else {
            minorThirdLabel.text = ""
        }
        // 5
        if (Bool.random()) {
            majorThirdLabel.text = "Major Third"
        } else {
            majorThirdLabel.text = ""
        }
        // 6
        if (Bool.random()) {
            perfectFourthLabel.text = "Perfect Fourth"
        } else {
            perfectFourthLabel.text = ""
        }
        // 7
        if (Bool.random()) {
            tritoneLabel.text = "Tritone"
        } else {
            tritoneLabel.text = ""
        }
        // 8
        if (Bool.random()) {
            perfectFifthLabel.text = "Perfect Fifth"
        } else {
            perfectFifthLabel.text = ""
        }
        // 9
        if (Bool.random()) {
            minorSixthLabel.text = "Minor Sixth"
        } else {
            minorSixthLabel.text = ""
        }
        // 10
        if (Bool.random()) {
            majorSixthLabel.text = "Major Sixth"
        } else {
            majorSixthLabel.text = ""
        }
        // 11
        if (Bool.random()) {
            minorSeventhLabel.text = "Minor Seventh"
        } else {
            minorSeventhLabel.text = ""
        }
        // 12
        if (Bool.random()) {
            majorSeventhLabel.text = "Major Seventh"
        } else {
            majorSeventhLabel.text = ""
        }
        // 13
        if (Bool.random()) {
            octaveLabel.text = "Octave"
        } else {
            octaveLabel.text = ""
        }
        
    }

}

