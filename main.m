//
//  main.m
//  getDockURL
//
//  Created by Fan Wang on 2015-11-22.
//  Copyright (c) 2015 Fan Wang. All rights reserved.
//

#import <Foundation/Foundation.h>
//@import AppKit;

int main(int argc, const char * argv[]) {
    /*NSWorkspace * ws = [NSWorkspace sharedWorkspace];
    NSArray * apps = [ws runningApplications];
        
    NSUInteger count = [apps count];
    [[NSFileManager defaultManager] createFileAtPath:@"./" contents:nil attributes:nil];
    for (NSUInteger i = 0; i < count; i++) {
        NSRunningApplication *app = [apps objectAtIndex: i ];
        NSString *str = app.bundleIdentifier;
        [str writeToFile:@"./" atomically: YES encoding:NSUTF8StringEncoding error:nil];
        NSLog(@"%@", app.bundleIdentifier);
        
        if (app.activationPolicy == NSApplicationActivationPolicyRegular) {
            NSLog(@"0");
        }
            
    }*/
    
    
    
    NSAppleScript *script = [[NSAppleScript alloc] initWithSource:@"tell application \"Safari\" to return URL of tabs of window 1"];
    NSDictionary *scriptError = nil;
    NSAppleEventDescriptor *descriptor = [script executeAndReturnError:&scriptError];
    if(scriptError) {
        NSLog(@"");
    } else {
        NSAppleEventDescriptor *listDescriptor = [descriptor  coerceToDescriptorType:typeAEList];
        NSMutableArray *result = [[NSMutableArray alloc] init];
        for (NSInteger i = 1; i <= [listDescriptor numberOfItems]; ++i) {
            NSAppleEventDescriptor *URLDescriptor = [listDescriptor descriptorAtIndex:i];
            [result addObject: URLDescriptor.stringValue];
        }
        
        NSString *content = [result componentsJoinedByString:@","];
        
        NSData *fileContents = [content dataUsingEncoding:NSUTF8StringEncoding];
        [[NSFileManager defaultManager] createFileAtPath:[@"~/Desktop/foo.txt" stringByExpandingTildeInPath]
                                                contents:fileContents
                                              attributes:nil];
        NSLog(@"Result: %@", [result copy]);
    }
    return 0;
}

